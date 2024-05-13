from pathlib import Path

from rdflib import Graph, Namespace
from rdflib.compare import isomorphic

from rdflib.namespace import SDO

from src.dawe_nrm import api
from src.dawe_nrm.api.utils import (
    fetch_and_check_uri,
    fetch_collection_url_and_member_labels,
    fetch_lut_with_metadata,
)

default_path = Path("vocab_files/categorical_collections/luts")

URNPROPERTY = Namespace("urn:property:")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-p", "--path", dest="path", help="write to path")
    parser.add_argument(
        "-v",
        "--validate",
        dest="validate",
        action="store_true",
        help="validate the remote data with the local data",
    )

    args = parser.parse_args()

    cwd = Path.cwd()
    path = cwd / args.path if args.path else default_path
    path.mkdir(exist_ok=True)

    validate = args.validate

    api.categorical_values.write_all(path)

    if validate:
        if path == default_path:
            raise ValueError(
                "In order to validate local and remote LUTs, the path must be different to the default path."
            )

        print("Checking for changes...")

        # TODO: only fetch partial data from local graphs
        local_files = default_path.glob("**/*.ttl")
        local_lut_graph = Graph()
        local_lut_graph.bind("urnp", URNPROPERTY)
        for file in local_files:
            local_lut_graph.parse(file, format="turtle")

        local_graph = Graph()
        local_graph.bind("urnp", URNPROPERTY)

        for endpoint in api.categorical_values.endpoints:
            if fetch_and_check_uri(endpoint.endpoint_url):
                local_graph = fetch_lut_with_metadata(
                    local_lut_graph, endpoint.endpoint_url, local_graph
                )
            else:
                local_graph = fetch_collection_url_and_member_labels(
                    local_lut_graph, endpoint.endpoint_url, local_graph
                )

        remote_files = path.glob("**/*.ttl")
        remote_graph = Graph()
        for file in remote_files:
            remote_graph.parse(file, format="turtle")

        # Delete schema:url values since they would be different as they are
        # are added during transformation of the LUT API data to local files.
        # The reason they are different is because the value of schema:url
        # is tied to the file path on disk.
        local_graph.remove((None, SDO.url, None))
        remote_graph.remove((None, SDO.url, None))

        # Check for changes
        IS_ISOMORPHIC = isomorphic(local_graph, remote_graph)
        try:
            if not IS_ISOMORPHIC:
                local_graph_diff = local_graph - remote_graph
                remote_graph_diff = remote_graph - local_graph

                local_graph_diff.serialize("local_graph_diff.ttl", format="turtle")
                remote_graph_diff.serialize("remote_graph_diff.ttl", format="turtle")

                raise ValueError(
                    "🛑 The local and remote LUT data is different.\n"
                    f"Number of triples only in local: {len(local_graph_diff)}\n"
                    f"Number of triples only in remote: {len(remote_graph_diff)}"
                    "Differences have been written to the following files: local_graph_diff.ttl, remote_graph_diff.ttl"
                )
            else:
                print("Local and remote data is isomorphic 🎉")
        finally:
            # Clean up
            for file in path.glob("**/*"):
                file.unlink()
            path.rmdir()
    else:
        print(f"✅ LUTs written to {path.absolute()}")
