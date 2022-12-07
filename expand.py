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
        dest="filename",
        help="Filename of new data in the expanded graph.",
    )

    args = parser.parse_args()
    filename = args.filename

    path = "vocab_files"
    vocab_files_dir = Path(path)
    files = list(vocab_files_dir.glob("**/*.ttl"))
    graph = Graph()
    for file in files:
        graph.parse(file, format="turtle")

    print(f"Initial size: {len(graph)}")

    new_data_graph = Graph()
    new_data_graph.bind("tern", URIRef("https://w3id.org/tern/ontologies/tern/"))
    expand_graph(graph, new_data_graph)

    print(f"Final size: {len(graph) + len(new_data_graph)}")
    graph.serialize("dump.ttl", format="turtle")
    date_today = date.today()

    new_data_graph.serialize(filename, format="turtle")
    print(f"New data in expanded graph written to {filename}")
