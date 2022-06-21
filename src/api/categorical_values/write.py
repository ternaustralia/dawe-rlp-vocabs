from pathlib import Path

from rdflib import URIRef
from rdflib.namespace import SKOS
from rich.progress import track

from src import api
from src.graph import NRM, create_graph, serialize
from src.schemas import LUTSchema


def write_all(path: Path, show_progress: bool = True):
    top_level_collection_member_graph = create_graph()
    top_level_collection_uri = URIRef(
        "https://linked.data.gov.au/def/test/dawe-cv/05f83f99-1998-4d11-8837-bb4a68788521"
    )

    def generate(lut_endpoint: LUTSchema):
        try:
            graph = api.categorical_values.get(NRM, lut_endpoint)

            label = lut_endpoint.uuid_namespace.replace(" ", "-") + ".ttl"
            if label == "collection.ttl":
                raise ValueError(
                    "Categorical values collection cannot be named collection.ttl as it is already reserved for the top-level collection."
                )
            serialize(path / label, graph)

            top_level_collection_member_graph.add(
                (
                    top_level_collection_uri,
                    SKOS.member,
                    NRM[lut_endpoint.collection_uuid],
                )
            )
        except api.categorical_values.exceptions.NoDataInAPIException as err:
            raise Exception(err) from err

    if show_progress:
        for lut_endpoint in track(
            api.categorical_values.endpoints,
            description=f"Pulling and writing LUTs to {path.absolute()}",
        ):
            generate(lut_endpoint)
    else:
        for lut_endpoint in api.categorical_values.endpoints:
            generate(lut_endpoint)

    serialize(path / "collection-members.ttl", top_level_collection_member_graph)
