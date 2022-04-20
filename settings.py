from os import environ

try:
    from dotenv import load_dotenv

    load_dotenv()
except ModuleNotFoundError:
    pass


GRAPHDB_URL = environ.get("GRAPHDB_URL", "http://localhost:7200/")
GRAPHDB_REPO_NAME = environ.get("GRAPHDB_REPO_NAME", "dawe_vocabs_core")
GRAPHDB_USERNAME = environ.get("GRAPHDB_USERNAME")
GRAPHDB_PASSWORD = environ.get("GRAPHDB_PASSWORD")
