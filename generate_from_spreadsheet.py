# download the spreadsheet
# import logging
import pathlib
from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth
from oauth2client.service_account import ServiceAccountCredentials
from dawe_vocabs.schemas import ExcelVocab

pathlib.Path("test/google").mkdir(parents=True, exist_ok=True)
scope = ["https://www.googleapis.com/auth/drive"]
gauth = GoogleAuth()
gauth.auth_method = "service"
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "client_secrets.json", scope
)
drive = GoogleDrive(gauth)
spreadsheet = [
    ExcelVocab(
        r"Stage2-DAWE protocols vocabs mapping - Arun.xlsx",
        "1JXP16wh1IG4i9-mdL_xOCJc60Y6vhQMiloCV0d0SIjw",
    )
]
for file in spreadsheet:
    # logger.info(f"Downloading {file.path} with id {file.id}")
    drive_file = drive.CreateFile({"id": file.id})
    drive_file.GetContentFile(
        file.path,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


# def check_module_names(file_name, lst, modules):
#     for i in lst:
#         if i not in modules:
#             print(file_name, " -- incorrect module names: ", i)

# # read the data from the spreadsheet

# from cmath import nan
# import pandas as pd

# xls = pd.ExcelFile("spreadsheet.xlsx")
# mapping_df = pd.read_excel(xls, "Mapping")
# property_df = pd.read_excel(xls, "Observable Properties-definitio")
# attribute_df = pd.read_excel(xls, "Attributes - definition")
# # print(mapping_df, property_df, attribute_df)

# # make a list of needed modules
# modules = [
#     "Basal area module",
#     "Coarse Woody Debris module",
#     "Condition Module",
#     "Fire Module",
#     "Soil module",
#     "Soil module - Plot soil description protocol",
#     "Soil module - soil pit characterization protocol",
#     "Soil module - soil subsite sampling protocol",
#     "Soil module- soil bulk density protocol",
# ]

# # make sure module names in three files are correct
# check_module_names("Mapping", mapping_df["modules"].unique().tolist(), modules)
# check_module_names("Attribute", attribute_df["Module Name"].unique().tolist(), modules)
# check_module_names("Property", property_df["Module Name"].unique().tolist(), modules)
