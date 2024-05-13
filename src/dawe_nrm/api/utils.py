import uuid
from rdflib import URIRef, SKOS, Namespace
import requests


def get_local_uuid_name(id):
    """Use an id to seed the generation of a uuid5."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, id))


def generate_combined_uri(uri1, uri2):
    # Extract UUIDs from the provided URIs
    uuid1 = uri1.split("/")[-1]
    uuid2 = uri2.split("/")[-1]

    # Construct the combined URI
    combined_uri = URIRef(f"urn:lut-check:{uuid1}:{uuid2}")

    return combined_uri


def fetch_and_check_uri(endpoint_url):
    try:
        # Fetch JSON data from the API endpoint
        response = requests.get(endpoint_url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        if isinstance(data, list):
            # Strapi3
            rows = data
        else:
            if data.get("data"):
                # Strapi4
                rows = data["data"]
            else:
                rows = None

        # Check if all rows have values for the 'uri' attribute
        return all("uri" in row and row["uri"] for row in rows)

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return False


def fetch_collection_url_and_member_labels(
    local_lut_graph, collection_url, local_graph
):

    collection_url = URIRef(collection_url)

    for s, p, o in local_lut_graph.triples((collection_url, SKOS.member, None)):
        for ss, pp, oo in local_lut_graph.triples((o, SKOS.prefLabel, None)):
            local_graph.add((collection_url, SKOS.member, oo))

    return local_graph


def fetch_lut_with_metadata(local_lut_graph, collection_url, local_graph):

    collection_url = URIRef(collection_url)

    URNPROPERTY = Namespace("urn:property:")

    for s, p, o in local_lut_graph.triples((collection_url, SKOS.member, None)):
        local_graph.add((collection_url, SKOS.member, o))
        local_graph.add((o, SKOS.prefLabel, local_lut_graph.value(o, SKOS.prefLabel)))

        meta_uri = generate_combined_uri(str(collection_url), str(o))
        local_graph.add((meta_uri, URNPROPERTY.categoricalCollection, collection_url))
        local_graph.add((meta_uri, URNPROPERTY.categoricalConcept, o))

        for s1, p1, o1 in local_lut_graph.triples((None, None, None)):
            if (p1, o1) == (URNPROPERTY.categoricalCollection, collection_url) and (
                p1,
                o1,
            ) == (URNPROPERTY.categoricalConcept, o):
                for s2, p2, o2 in local_lut_graph.triples((s, None, None)):
                    if p2 == URNPROPERTY.conceptDefinition:
                        local_graph.add((meta_uri, URNPROPERTY.conceptDefinition, o2))
                    elif p2 == URNPROPERTY.conceptNotation:
                        local_graph.add((meta_uri, URNPROPERTY.conceptNotation, o2))

    return local_graph
