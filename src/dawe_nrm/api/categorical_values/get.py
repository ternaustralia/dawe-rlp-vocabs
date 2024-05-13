# Please DO NOT run this function to fetch LUTs, categorical concepts information is not dependent on external APIs now.

import httpx
from rdflib import DCTERMS, RDF, SKOS, Graph, Literal, Namespace, URIRef

from src.dawe_nrm.api.categorical_values.exceptions import NoDataInAPIException
from src.dawe_nrm.api.utils import get_local_uuid_name, generate_combined_uri
from src.dawe_nrm.graph import create_graph
from src.dawe_nrm.schemas import LUTSchema


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

    collection_uri = URIRef(config.collection_url)

    # URNCLASS = Namespace("urn:class:")
    URNPROPERTY = Namespace("urn:property:")
    graph = create_graph()
    # graph.bind("urnc", URNCLASS)
    graph.bind("urnp", URNPROPERTY)

    if all("uri" in row and row["uri"] for row in rows):

        print(collection_uri)

        concepts = []

        # # URNCLASS = Namespace("urn:class:")
        # URNPROPERTY = Namespace("urn:property:")
        # graph = create_graph()
        # # graph.bind("urnc", URNCLASS)
        # graph.bind("urnp", URNPROPERTY)

        # Create the collection
        # collection_uri = URIRef(config.collection_url)
        # graph.add((collection_uri, DCTERMS.source, URIRef(config.endpoint_url)))
        # graph.add((collection_uri, RDF.type, SKOS.Collection))
        # graph.add((collection_uri, SKOS.prefLabel, Literal(config.label)))
        # graph.add(
        #     (
        #         collection_uri,
        #         DCTERMS.description,
        #         Literal(config.description),
        #     )
        # )

        for row in rows:
            # Get categorical values information from API
            if row.get("attributes"):
                label = row["attributes"]["label"].lower()
                symbol = row["attributes"]["symbol"]
                # if row["attributes"].get("tree_description"):
                #     # See LUTSchema for <https://core.vocabs.paratoo.tern.org.au/api/lut-targeted-survey-flora-growth-stages>
                #     description = (
                #         "Tree description: "
                #         + row["attributes"]["tree_description"]
                #         + ".  "
                #         + "Shrub description: "
                #         + row["attributes"]["shrub_description"]
                #         + ". "
                #     )
                # else:
                description = row["attributes"]["description"]
                uri = row["attributes"]["uri"]
            else:
                label = row["label"].lower()
                description = row["description"]
                symbol = row["symbol"]
                uri = row["uri"]

            # Generate uuid based on labels to avoid duplicates
            # local_name = get_local_uuid_name(f"{label}")
            # concept_uri = base_uri[local_name]
            concept_uri = URIRef(uri)
            concepts.append(concept_uri)

            # Add concept in collection
            # graph.add((concept_uri, RDF.type, SKOS.Concept))
            graph.add((concept_uri, SKOS.prefLabel, Literal(label)))
            # graph.add((concept_uri, SKOS.definition, Literal(description)))
            # graph.add((concept_uri, SKOS.notation, Literal(symbol)))
            # graph.add((concept_uri, DCTERMS.identifier, Literal(row["id"])))
            # graph.add(
            #     (
            #         concept_uri,
            #         DCTERMS.source,
            #         URIRef(config.endpoint_url),
            #     )
            # )

            # Generate the collection specific URI for concept
            # if row.get("attributes") and row["attributes"].get("uuid"):
            #     concept_name_by_collection = row["attributes"]["uuid"]
            # else:
            #     # Use this temporarily until the "uuid" field is available in the API.
            #     concept_name_by_collection = get_local_uuid_name(
            #         f"{config.uuid_namespace}-{row['id']}"
            #     )
            # concept_uri_by_collection = base_uri[concept_name_by_collection]

            concept_uri_by_collection = generate_combined_uri(
                str(collection_uri), str(concept_uri)
            )

            # Create collection specific information for each concept
            # graph.add(
            #     (concept_uri_by_collection, RDF.type, URNCLASS.CategoricalConceptMeta)
            # )
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
                (
                    concept_uri_by_collection,
                    URNPROPERTY.conceptNotation,
                    Literal(symbol),
                )
            )
            # graph.add(
            #     (
            #         concept_uri_by_collection,
            #         URNPROPERTY.conceptIdentifier,
            #         Literal(row["id"]),
            #     )
            # )
            # graph.add(
            #     (
            #         concept_uri_by_collection,
            #         URNPROPERTY.conceptSource,
            #         URIRef(config.endpoint_url),
            #     )
            # )

        for concept in concepts:
            graph.add((collection_uri, SKOS.member, concept))
    else:
        for row in rows:
            # Get categorical values information from API
            if row.get("attributes"):
                label = row["attributes"]["label"].lower()
            else:
                label = row["label"].lower()

            graph.add((collection_uri, SKOS.member, Literal(label)))

    return graph
