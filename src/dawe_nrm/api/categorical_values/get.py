# Please DO NOT run this function to fetch LUTs, categorical concepts information is not dependent on external APIs now.

import httpx
from rdflib import DCTERMS, RDF, SKOS, Graph, Literal, Namespace, URIRef

from src.dawe_nrm.api.categorical_values.exceptions import NoDataInAPIException
from src.dawe_nrm.api.utils import generate_combined_uri
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

    URNPROPERTY = Namespace("urn:property:")
    graph = create_graph()
    graph.bind("urnp", URNPROPERTY)

    if all("uri" in row["attributes"] and row["attributes"]["uri"] for row in rows):

        concepts = []

        for row in rows:
            # Get categorical values information from API
            if row.get("attributes"):
                label = row["attributes"]["label"].lower()
                symbol = row["attributes"]["symbol"]
                description = row["attributes"]["description"]
                uri = row["attributes"]["uri"]
            else:
                label = row["label"].lower()
                description = row["description"]
                symbol = row["symbol"]
                uri = row["uri"]

            concept_uri = URIRef(uri)
            concepts.append(concept_uri)

            graph.add((concept_uri, SKOS.prefLabel, Literal(label)))

            concept_uri_by_collection = generate_combined_uri(
                str(collection_uri), str(concept_uri)
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
                (
                    concept_uri_by_collection,
                    URNPROPERTY.conceptNotation,
                    Literal(symbol),
                )
            )

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
