import httpx
from rdflib import DCTERMS, RDF, SKOS, Graph, Literal, Namespace, URIRef

from dawe_nrm.api.categorical_values.exceptions import NoDataInAPIException
from dawe_nrm.api.utils import get_local_uuid_name
from dawe_nrm.graph import create_graph
from dawe_nrm.schemas import LUTSchema


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

    URNCLASS = Namespace("urn:class:")
    URNPROPERTY = Namespace("urn:property:")
    graph = create_graph()
    graph.bind("urnc", URNCLASS)
    graph.bind("urnp", URNPROPERTY)

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

    for row in rows:
        # Get categorical values information from API
        if row.get("attributes"):
            label = row["attributes"]["label"]
            symbol = row["attributes"]["symbol"]
            if row["attributes"].get("tree_description"):
                # See LUTSchema for <https://core.vocabs.paratoo.tern.org.au/api/lut-targeted-survey-flora-growth-stages>
                description = (
                    "Tree description: "
                    + row["attributes"]["tree_description"]
                    + ".  "
                    + "Shrub description: "
                    + row["attributes"]["shrub_description"]
                    + ". "
                )
            else:
                description = row["attributes"]["description"]
        else:
            label = row["label"]
            description = row["description"]
            symbol = row["symbol"]

        # Generate uuid based on labels to avoid duplicates
        local_name = get_local_uuid_name(f"{label}")
        concept_uri = base_uri[local_name]
        concepts.append(concept_uri)

        # Add concept in collection
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

        # Generate the collection specific URI for concept
        if row.get("attributes") and row["attributes"].get("uuid"):
            concept_name_by_collection = row["attributes"]["uuid"]
        else:
            # Use this temporarily until the "uuid" field is available in the API.
            concept_name_by_collection = get_local_uuid_name(
                f"{config.uuid_namespace}-{row['id']}"
            )
        concept_uri_by_collection = base_uri[concept_name_by_collection]

        # Create collection specific information for each concept
        graph.add(
            (concept_uri_by_collection, RDF.type, URNCLASS.CategoricalConceptMeta)
        )
        graph.add(
            (concept_uri_by_collection, URNPROPERTY.categoricalConcept, concept_uri)
        )
        graph.add(
            (
                concept_uri_by_collection,
                URNPROPERTY.categoricalCollection,
                collection_uri,
            )
        )
        graph.add(
            (
                concept_uri_by_collection,
                URNPROPERTY.conceptDefinition,
                Literal(description),
            )
        )
        graph.add(
            (concept_uri_by_collection, URNPROPERTY.conceptNotation, Literal(symbol))
        )
        graph.add(
            (
                concept_uri_by_collection,
                URNPROPERTY.conceptIdentifier,
                Literal(row["id"]),
            )
        )
        graph.add(
            (
                concept_uri_by_collection,
                URNPROPERTY.conceptSource,
                URIRef(config.endpoint_url),
            )
        )

    for concept in concepts:
        graph.add((collection_uri, SKOS.member, concept))

    return graph
