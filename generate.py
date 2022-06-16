"""
Generate RDF from Excel files using excel2rdf with data validation provided by PySHACL.
"""

import logging
import pathlib
from numpy import NaN

from rdflib import Graph, SKOS, DCTERMS, SH
from excel2rdf import excel2rdf
from pyshacl import validate
from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

from dawe_vocabs import settings
from dawe_vocabs.namespaces import TERN, REG
from dawe_vocabs.pretty_table import get_pretty_table_output
from dawe_vocabs.schemas import LUTSchema
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

    # Details for service account usage from PR at
    # https://github.com/iterative/PyDrive2/blob/e56591edb79bdbe7df147839b5e4dd3e866ad8c3/docs/quickstart.rst
    if settings.download_excel_files:
        scope = ["https://www.googleapis.com/auth/drive"]
        gauth = GoogleAuth()
        gauth.auth_method = "service"
        gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "client_secrets.json", scope
        )
        drive = GoogleDrive(gauth)

        for file in settings.excel_files:
            logger.info("Downloading %s with id %s", file.path, file.id)
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
            raise RuntimeError(f'Error with file "{path}". {e}') from e

    # Programatically create some vocabs.
    feature_types_collection.create(settings.base_uri, g)

    # get settings.lut_configs and prepare to extend
    lut_configs = settings.lut_configs

    # extend lut_configs in settings with new categorical APIs
    # xls = pd.ExcelFile("spreadsheet.xlsx")
    # mapping_df = pd.read_excel(xls, "Mapping")
    # mapping_df = mapping_df.reset_index()
    # names = []
    # for i in settings.modules:
    #     names.append(i.name)
    # for index, row in mapping_df.iterrows():
    #     categorical_api = (
    #         row["categorical_lut_api_endpoint"].strip()
    #         if isinstance(row["categorical_lut_api_endpoint"], str)
    #         else row["categorical_lut_api_endpoint"]
    #     )
    #     if row["observable_property_in_protocol"] is NaN:
    #         label = row["attribute_in_protocol"]
    #     else:
    #         label = row["observable_property_in_protocol"]
    #     if (
    #         (row["modules"] in names)
    #         and (row["modules"] not in settings.categorical_apis_added_modules)
    #         and (categorical_api is not NaN)
    #         and (label not in settings.deleted_parameters)
    #     ):
    #         categorical_api_label = " ".join(
    #             str(categorical_api).split("/")[-1].split("-")[1:]
    #         )
    #         lut_configs.append(
    #             LUTSchema(
    #                 categorical_api,
    #                 categorical_api_label.capitalize() + " codes",
    #                 "A collection of " + categorical_api_label + " and its codes.",
    #                 str(row["categorical_uuid"]),
    #                 categorical_api_label.capitalize(),
    #             )
    #         )

    # Generate look up tables to categorical values.
    for lut_config in lut_configs:
        logger.info("Pulling LUT data from %s", lut_config.endpoint_url)
        try:
            categorical_values_collection.create(
                settings.base_uri, g, lut_config, settings.parent_collection_uri
            )
        except categorical_values_collection.NoDataInAPIException as e:
            logger.error(e)
        except Exception as e:
            raise RuntimeError(f'Error with LUT config "{lut_config}". {e}') from e

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
        TABLE_RESULT = get_pretty_table_output(conforms, results_graph)
        logger.info(TABLE_RESULT)
    else:
        logger.info("\n%s", results_text)

    logger.info("PySHACL conforms output: %s", conforms)
    logger.info("sh:Violation exists: %s", bool(violation))
    logger.info("sh:Warning exists: %s", bool(warning))
    logger.info("sh:Info exists: %s", bool(info))

    # Load in the custom controlled vocabularies created in this repo.
    custom_vocabs_dir = pathlib.Path.cwd() / "dawe_vocabs" / "custom_vocabs"
    custom_vocab_files = [
        file for file in custom_vocabs_dir.iterdir() if file.is_file()
    ]
    for file in custom_vocab_files:
        g.parse(file, format="turtle")

    g.serialize(settings.output_filename)
