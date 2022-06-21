from requests.exceptions import HTTPError
from dawe_nrm.graphdb import repository

try:
    repository.create("http://localhost:7200/", "dawe_vocabs_core", "test1")
except HTTPError:
    pass

with open("output.ttl", "r", encoding="utf-8") as f:
    repository.insert(
        "http://localhost:7200/",
        "dawe_vocabs_core",
        f.read().encode("utf-8"),
        "text/turtle",
    )
