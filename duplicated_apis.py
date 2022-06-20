import re
import uuid
import logging
import requests
from typing import List
from rdflib import Graph, SKOS, DCTERMS, SH

from dawe_vocabs import settings
from dawe_vocabs.schemas import LUTSchema
from dawe_vocabs.namespaces import TERN, REG
from dawe_vocabs.vocabs import categorical_values_collection

url = "http://vocabs.paratoo.tern.org.au:1337/documentation"
r = requests.get(url)
result = r.text

lut_indexes = [m.start() for m in re.finditer('"/lut-', result)]

lut_labels = []

for i in range(len(lut_indexes) - 1):
    label = re.search('"/lut-(.*?)"', result[lut_indexes[i] : lut_indexes[i + 1]])
    if "/{" not in label.group(1):
        lut_labels.append("lut-" + label.group(1))

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("duplicated_apis.py")

    g = Graph()
    g.bind("tern", TERN)
    g.bind("skos", SKOS)
    g.bind("dct", DCTERMS)
    g.bind("reg", REG)

    lut_configs: List[LUTSchema] = []

    for lut_label in lut_labels:
        categorical_api_label = " ".join(lut_label.split("-")[1:])
        lut_configs.append(
            LUTSchema(
                "http://vocabs.paratoo.tern.org.au:1337/api/" + lut_label,
                categorical_api_label.capitalize() + " codes",
                "A collection of " + categorical_api_label + " and its codes.",
                str(uuid.uuid4()),
                categorical_api_label.capitalize(),
            )
        )

    non_data_luts = []
    runtime_luts = []

    for lut_config in lut_configs:
        logger.info("Pulling LUT data from %s", lut_config.endpoint_url)
        try:
            categorical_values_collection.create(
                settings.base_uri, g, lut_config, settings.parent_collection_uri
            )
        except categorical_values_collection.NoDataInAPIException as e:
            non_data_luts.append(lut_config.endpoint_url)
            logger.error(e)
        except Exception as e:
            runtime_luts.append(lut_config.endpoint_url)
            raise RuntimeError(f'Error with LUT config "{lut_config}". {e}') from e

    print("Number of endpoints without data: " + str(len(non_data_luts)))
    print(non_data_luts)
    print("Number of endpoints with runtime error: " + str(len(runtime_luts)))
    print(runtime_luts)

    # g.serialize("luts.ttl")
