import requests
from rdflib import Graph, Namespace, URIRef, Literal, RDF, SKOS, DCTERMS

from dawe_vocabs.schemas import LUTSchema
from dawe_vocabs.vocabs.common import get_local_uuid_name


class NoDataInAPIException(Exception):
    """This is raised when no data is received from the API."""

    pass


class UnexpectedDataShapeException(Exception):
    """This is raised when the shape of the data (JSON) is not the expected shape."""


def create(
    base_uri: Namespace, g: Graph, config: LUTSchema, parent_collection_uri: str
) -> None:
    r = requests.get(config.endpoint_url)
    r.raise_for_status()

    data = r.json()

    if isinstance(data, list):
        # Strapi3
        rows = data
    else:
        if data.get("data"):
            # Strapi4
            rows = data["data"]
        else:
            raise UnexpectedDataShapeException(
                "Expected the JSON object to have a 'data' key but none was found."
            )

    if not rows:
        raise NoDataInAPIException(
            f"API endpoint {config.endpoint_url} returned no data."
        )

    concepts = list()

    for row in rows:
        if row.get("attributes") and row["attributes"].get("uuid"):
            local_name = row["attributes"]["uuid"]
        else:
            # Use this temporarily until the "uuid" field is available from the API.
            local_name = get_local_uuid_name(f"{config.uuid_namespace}-{row['id']}")
        concept_uri = base_uri[local_name]
        concepts.append(concept_uri)

        if row.get("attributes"):
            label = row["attributes"]["label"]
            description = row["attributes"]["description"]
            symbol = row["attributes"]["symbol"]
        else:
            label = row["label"]
            description = row["description"]
            symbol = row["symbol"]

        g.add((concept_uri, RDF.type, SKOS.Concept))
        g.add((concept_uri, SKOS.prefLabel, Literal(label)))
        g.add((concept_uri, SKOS.definition, Literal(description)))
        g.add((concept_uri, SKOS.notation, Literal(symbol)))
        g.add((concept_uri, DCTERMS.identifier, Literal(row["id"])))
        g.add(
            (
                concept_uri,
                DCTERMS.source,
                URIRef(config.endpoint_url),
            )
        )

    # Create the collection
    collection_uri = base_uri[config.collection_uuid]
    g.add((collection_uri, DCTERMS.source, URIRef(config.endpoint_url)))
    g.add((URIRef(parent_collection_uri), SKOS.member, collection_uri))
    g.add((collection_uri, RDF.type, SKOS.Collection))
    g.add((collection_uri, SKOS.prefLabel, Literal(config.label)))
    g.add(
        (
            collection_uri,
            DCTERMS.description,
            Literal(config.description),
        )
    )
    for concept in concepts:
        g.add((collection_uri, SKOS.member, concept))
