from requests.exceptions import HTTPError

from src.graphdb import repository
import settings

try:
    repository.create(
        settings.GRAPHDB_URL,
        settings.GRAPHDB_REPO_NAME,
        settings.GRAPHDB_REPO_NAME,
        auth=(settings.GRAPHDB_USERNAME, settings.GRAPHDB_PASSWORD),
    )
except HTTPError:
    pass

with open("output.ttl", "r", encoding="utf-8") as f:
    repository.insert(
        settings.GRAPHDB_URL,
        settings.GRAPHDB_REPO_NAME,
        f.read().encode("utf-8"),
        "text/turtle",
        auth=(settings.GRAPHDB_USERNAME, settings.GRAPHDB_PASSWORD),
        context="<https://linked.data.gov.au/def/test/dawe-cv/>"
    )
