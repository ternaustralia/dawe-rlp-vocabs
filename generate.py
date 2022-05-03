"""
Generate RDF from Excel files using excel2rdf with data validation provided by PySHACL.
"""

import logging
import pathlib

from rdflib import Graph, SKOS, DCTERMS, SH
from excel2rdf import excel2rdf
from pyshacl import validate
from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth
from oauth2client.service_account import ServiceAccountCredentials

from dawe_vocabs import settings
from dawe_vocabs.namespaces import TERN, REG
from dawe_vocabs.pretty_table import get_pretty_table_output
from dawe_vocabs.vocabs import feature_types_collection
from dawe_vocabs.vocabs import categorical_values_collection


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("generate.py")

    g = Graph()
    g.bind("tern", TERN)
    g.bind("skos", SKOS)
    g.bind("dct", DCTERMS)
    g.bind("reg", REG)

    # Download Excel vocab files and store to disk.
    # Create directory if not exists.
    pathlib.Path(settings.excel_files_dir_first).mkdir(parents=True, exist_ok=True)
    pathlib.Path(settings.excel_files_dir_second).mkdir(parents=True, exist_ok=True)

    # Details for service account usage from PR at https://github.com/iterative/PyDrive2/blob/e56591edb79bdbe7df147839b5e4dd3e866ad8c3/docs/quickstart.rst
    if settings.download_excel_files:
        scope = ["https://www.googleapis.com/auth/drive"]
        gauth = GoogleAuth()
        gauth.auth_method = "service"
        gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "client_secrets.json", scope
        )
        drive = GoogleDrive(gauth)

        for file in settings.excel_files:
            logger.info(f"Downloading {file.path} with id {file.id}")
            drive_file = drive.CreateFile({"id": file.id})
            drive_file.GetContentFile(file.path)

    # # Create vocabs from Excel files.
    # for file in settings.excel_files:
    #     try:
    #         g += excel2rdf(file.path)
    #     except Exception as e:
    #         raise RuntimeError(f'Error with file "{file}". {e}')

    from pathlib import Path

    pathlist = Path("vocab-sources").rglob("*.xlsx")
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        # print(path_in_str)
        try:
            g += excel2rdf(path_in_str)
        except Exception as e:
            raise RuntimeError(f'Error with file "{path_in_str}". {e}')

    # Programatically create some vocabs.
    feature_types_collection.create(settings.base_uri, g)

    # Generate look up tables to categorical values.
    for lut_config in settings.lut_configs:
        try:
            categorical_values_collection.create(
                settings.base_uri, g, lut_config, settings.parent_collection_uri
            )
        except categorical_values_collection.NoDataInAPIException as e:
            logger.error(e)
        except Exception as e:
            raise RuntimeError(f'Error with file "{file}". {e}')

    # Validate generated data based on vocab requirements.
    shacl_graph = Graph().parse(settings.shapes_file)
    conforms, results_graph, results_text = validate(
        g,
        shacl_graph=shacl_graph,
    )

    violation = results_graph.value(None, SH.resultSeverity, SH.Violation)
    warning = results_graph.value(None, SH.resultSeverity, SH.Warning)
    info = results_graph.value(None, SH.resultSeverity, SH.Info)

    if settings.show_table_result:
        table_result = get_pretty_table_output(conforms, results_graph)
        logger.info(table_result)

    logger.info(f"PySHACL conforms output: {conforms}")
    logger.info(f"sh:Violation exists: {True if violation else False}")
    logger.info(f"sh:Warning exists: {True if warning else False}")
    logger.info(f"sh:Info exists: {True if info else False}")

    g.serialize(settings.output_filename)
