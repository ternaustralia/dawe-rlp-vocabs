from argparse import ArgumentParser
from datetime import date
from pathlib import Path

from rdflib import Graph, URIRef

from dawe_nrm.expand_graph import expand_graph

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Load the vocabs data and expand the graph and write the new statements into a separate file."
    )
    parser.add_argument(
        dest="expand_type",
        help="The expand type, either for observable properties (OP) or categorical concepts (LUT).",
    )
    parser.add_argument(
        dest="filename",
        help="Filename of new data in the expanded graph.",
    )

    args = parser.parse_args()
    expand_type = args.expand_type
    filename = args.filename

    if expand_type == "OP":
        paths = [
            "vocab_files/observable_properties_by_module",
            "vocab_files/observable_property_concepts",
        ]
    elif expand_type == "LUT":
        paths = [
            "vocab_files/categorical_collections",
        ]
    elif expand_type == "A":
        paths = ["vocab_files/attribute_concepts", "vocab_files/attributes_by_module"]
    elif expand_type == "M":
        paths = ["vocab_files/methods_by_module"]
    else:
        raise ValueError(
            "The expand type is incorrect, options are 'OP' (observable properties), 'LUT' (categorical concepts), 'A' (Attributes), 'M' (Methods)."
        )

    graph = Graph()
    for path in paths:
        vocab_files_dir = Path(path)
        files = list(vocab_files_dir.glob("**/*.ttl"))
        for file in files:
            graph.parse(file, format="turtle")

    print(f"Initial size: {len(graph)}")

    new_data_graph = Graph()
    new_data_graph.bind("tern", URIRef("https://w3id.org/tern/ontologies/tern/"))
    expand_graph(graph, new_data_graph)

    print(f"Final size: {len(graph) + len(new_data_graph)}")
    date_today = date.today()

    new_data_graph.serialize(filename, format="turtle")
    print(f"New data in expanded graph written to {filename}")
