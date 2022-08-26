import httpx
from rdflib import DCTERMS, RDF, SKOS, Graph, Literal, Namespace, URIRef, XSD, RDFS

from dawe_nrm.api.categorical_values.exceptions import NoDataInAPIException
from dawe_nrm.api.utils import get_local_uuid_name
from dawe_nrm.graph import create_graph
from dawe_nrm.schemas import LUTSchema

SCHEMA = Namespace("https://schema.org/")


async def get(
    base_uri: Namespace, config: LUTSchema, client: httpx.AsyncClient
) -> Graph:
    response = await client.get(config.endpoint_url)
    response.raise_for_status()

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

    if not rows:
        raise NoDataInAPIException(
            f"API endpoint {config.endpoint_url} returned no data."
        )

    concepts = []
    graph = create_graph()

    for row in rows:
        if row.get("attributes") and row["attributes"].get("uuid"):
            local_name = row["attributes"]["uuid"]
        else:
            # Use this temporarily until the "uuid" field is available in the API.
            local_name = get_local_uuid_name(f"{config.uuid_namespace}-{row['id']}")
        concept_uri = base_uri[local_name]
        concepts.append(concept_uri)

        if row.get("attributes"):
            label = row["attributes"]["label"]
            symbol = row["attributes"]["symbol"]
            if row["attributes"].get("tree_description"):
                description = (
                    "Tree description: "
                    + row["attributes"]["tree_description"]
                    + ".  "
                    + row["attributes"]["shrub_description"]
                    + ". "
                )
            else:
                description = row["attributes"]["description"]
        else:
            label = row["label"]
            description = row["description"]
            symbol = row["symbol"]

        graph.add((concept_uri, RDF.type, SKOS.Concept))
        graph.add((concept_uri, SKOS.prefLabel, Literal(label)))
        graph.add((concept_uri, SKOS.definition, Literal(description)))
        graph.add((concept_uri, SKOS.notation, Literal(symbol)))
        graph.add((concept_uri, DCTERMS.identifier, Literal(row["id"])))
        graph.add(
            (
                concept_uri,
                DCTERMS.source,
                URIRef(config.endpoint_url),
            )
        )
        graph.add(
            (
                concept_uri,
                RDFS.isDefinedBy,
                URIRef("https://linked.data.gov.au/def/nrm/"),
            )
        )
        graph.add(
            (
                concept_uri,
                SCHEMA.url,
                Literal(
                    "https://github.com/ternaustralia/dawe-rlp-vocabs/tree/main/vocab_files/categorical_collections/luts/"
                    + config.uuid_namespace.replace(" ", "-")
                    + ".ttl",
                    datatype=XSD.anyURI,
                ),
            )
        )

    # Create the collection
    collection_uri = base_uri[config.collection_uuid]
    graph.add((collection_uri, DCTERMS.source, URIRef(config.endpoint_url)))
    graph.add((collection_uri, RDF.type, SKOS.Collection))
    graph.add((collection_uri, SKOS.prefLabel, Literal(config.label)))
    graph.add(
        (
            collection_uri,
            DCTERMS.description,
            Literal(config.description),
        )
    )
    graph.add(
        (
            collection_uri,
            RDFS.isDefinedBy,
            URIRef("https://linked.data.gov.au/def/nrm/"),
        )
    )
    graph.add(
        (
            collection_uri,
            SCHEMA.url,
            Literal(
                "https://github.com/ternaustralia/dawe-rlp-vocabs/tree/main/vocab_files/categorical_collections/luts/"
                + config.uuid_namespace.replace(" ", "-")
                + ".ttl",
                datatype=XSD.anyURI,
            ),
        )
    )
    for concept in concepts:
        graph.add((collection_uri, SKOS.member, concept))

    return graph
