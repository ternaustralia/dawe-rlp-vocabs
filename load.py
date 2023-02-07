from argparse import ArgumentParser
from pathlib import Path

from rdflib import Graph
from requests.exceptions import HTTPError

from dawe_nrm.graphdb import repository

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Upload the data in the vocab_files directory to a GraphDB or RDF4J database."
    )
    parser.add_argument(
        "--url",
        dest="url",
        default="http://localhost:7200",
        help="URL of GraphDB or RDF4J base URL [default: http://localhost:7200]",
    )
    parser.add_argument(
        "--repository",
        dest="repository_id",
        default="dawe_vocabs_core",
        help="The GraphDB or RDF4J repository ID [default: dawe_vocabs_core]",
    )
    parser.add_argument(
        "-u",
        "--username",
        dest="username",
        help="The username to use when interfaceing with GraphDB or RDF4J [default: None]",
    )
    parser.add_argument(
        "-p",
        "--password",
        dest="password",
        help="The password to use when interfaceing with GraphDB or RDF4J [default: None]",
    )

    args = parser.parse_args()
    url = args.url
    repository_id = args.repository_id
    username = args.username
    password = args.password

    try:
        repository.create(
            url,
            repository_id,
            "DAWE NRM controlled vocabularies",
            (username, password),
        )
    except HTTPError:
        # Repository already exists, probably.
        pass

    vocab_files_dir = Path("vocab_files")
    files = list(vocab_files_dir.glob("**/*.ttl"))

    graph = Graph()
    for file in files:
        graph.parse(file, format="turtle")

    data = graph.serialize(format="turtle", encoding="utf-8")

    repository.insert(
        url,
        repository_id,
        data,
        "text/turtle",
        "<https://linked.data.gov.au/def/nrm>",
        (username, password),
    )
