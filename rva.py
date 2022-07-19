import sys
from argparse import ArgumentParser
from datetime import date
from pathlib import Path

from rdflib import Graph
from rich import print
from rich.console import Console

from dawe_nrm import api

console = Console()

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Publish controlled vocabularies to Research Vocabularies Australia (RVA)."
    )
    parser.add_argument(
        dest="path",
        help="Path to the directory of RDF Turtle files to be published.",
    )
    parser.add_argument(
        dest="username",
        help="RVA built-in account's username.",
    )
    parser.add_argument(
        dest="password",
        help="RVA built-in account's password.",
    )
    parser.add_argument(
        dest="vocabulary_id",
        help="RVA vocabulary ID used to determine the owner.",
    )
    parser.add_argument(
        dest="version",
        help="Vocabulary version of the new publication. E.g., 1.1.0",
    )
    parser.add_argument(
        "-e",
        "--environment",
        dest="environment",
        default="test",
        help="RVA environment. Value must be one of [prod, test]. [default: test]",
    )
    parser.add_argument(
        "-u",
        "-upload-filename",
        dest="upload_filename",
        default="upload.ttl",
        help="Upload filename. [default: upload.ttl]",
    )

    args = parser.parse_args()

    path = args.path
    username = args.username
    password = args.password
    vocabulary_id = args.vocabulary_id
    version = args.version
    env = args.environment
    upload_filename = args.upload_filename

    auth = (username, password)
    dev = True if env == "test" else False

    try:
        result = api.rva.get_vocabulary(vocabulary_id, dev)
        try:
            owner = result["owner"]
        except KeyError as err:
            raise KeyError(
                f"Failed to get the owner of vocabulary_id '{vocabulary_id}' from RVA."
            ) from err

        vocab_files_dir = Path(path)
        files = list(vocab_files_dir.glob("**/*.ttl"))

        graph = Graph()
        for file in files:
            graph.parse(file, format="turtle")

        data = graph.serialize(format="turtle")

        upload_id, filename = api.rva.create_upload(
            data, upload_filename, owner, auth, dev=dev
        )

        metadata = api.rva.publish_new_vocabulary_version(
            vocabulary_id, upload_id, version, str(date.today()), auth, dev=True
        )

        print("Vocabulary published successfully.")
        base_rva_url = (
            "https://demo.vocabs.ardc.edu.au/" if dev else "https://vocabs.ardc.edu.au/"
        )
        print(f"View at {base_rva_url}/viewById/{vocabulary_id}")

    except Exception as err:
        console.print_exception(show_locals=True)
        sys.exit(1)
