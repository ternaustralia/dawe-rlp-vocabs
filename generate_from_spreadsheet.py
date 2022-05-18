# download the spreadsheet
# import logging
import pathlib
from re import T
from numpy import NaN
from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth
from oauth2client.service_account import ServiceAccountCredentials
from dawe_vocabs.schemas import ExcelVocab
import xlsxwriter


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
        "spreadsheet.xlsx",
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


def check_module_names(file_name, lst, modules):
    for i in lst:
        if i not in modules:
            print(file_name, " -- incorrect module names: ", i)


def check_value_type(dataframe, types: list, modules_names):
    incorrect_value_types = []
    for index, row in dataframe.iterrows():
        # print(row["modules"])
        if row["modules"] in modules_names:
            if row["value_type"].lower() not in types:
                incorrect_value_types.append(row["value_type"])
    # for value in values:
    #     if value not in types:
    #         incorrect_value_types.append(value)
    return incorrect_value_types


def check_feature_type(dataframe, modules_names):
    propeties_without_feature_type = []
    for index, row in dataframe.iterrows():
        if row["modules"] in modules_names:
            if row["observable_property_in_protocol"] is not NaN:
                # print(row["observable_property_in_protocol"])
                if row["_feature_type"] is NaN:
                    propeties_without_feature_type.append(
                        "{} : {}".format(
                            row["modules"], row["observable_property_in_protocol"]
                        )
                    )
    return propeties_without_feature_type


def find_empty_definitions(dataframe, modules_names):
    for index, row in dataframe.iterrows():
        if row["Module Name"] in modules_names:
            if row["Preferred Label"] is not NaN:
                if row["Definition"] is NaN:
                    print(
                        "Empty definition: {} -- {} -- {}".format(
                            index, row["Module Name"], row["Preferred Label"]
                        )
                    )


def check_uuids(dataframe, modules_names):
    parameters_without_uuids = []
    for index, row in dataframe.iterrows():
        if row["modules"] in modules_names:
            if row["variable_uuid"] is NaN:
                parameters_without_uuids.append(index)
    return parameters_without_uuids


def check_categorical_uuids(dataframe, modules_names):
    categorical_parameters_without_categorical_uuids = []
    for index, row in dataframe.iterrows():
        if row["modules"] in modules_names:
            if row["value_type"].lower() == "categorical":
                if row["categorical_uuid"] is NaN:
                    categorical_parameters_without_categorical_uuids.append(index)
    return categorical_parameters_without_categorical_uuids


def get_attribute_definition_source(attributes, module_name, label):
    separated_attribute_definition_df = [
        y for _, y in attributes.groupby("Module Name", as_index=True)
    ]
    for item in separated_attribute_definition_df:
        if item["Module Name"].unique()[0] == module_name:
            definitions = item
    definitions = definitions.reset_index()
    for index, row in definitions.iterrows():
        if (row["Module Name"] == module_name) and (row["Preferred Label"] == label):
            return row["Definition"], row["Source"]


def get_property_definition_source(properties, module_name, label):
    separated_property_definition_df = [
        y for _, y in properties.groupby("Module Name", as_index=True)
    ]
    for item in separated_property_definition_df:
        if item["Module Name"].unique()[0] == module_name:
            definitions = item
    definitions = definitions.reset_index()
    for index, row in definitions.iterrows():
        if (row["Module Name"] == module_name) and (row["Preferred Label"] == label):
            return row["Definition"], row["Source"]


def check_parameters_definition(mapping, attributes, properties, modules_names):
    print("Empty definitions for attributes")
    find_empty_definitions(attributes, modules_names)
    print("-------------------------------------------------------")
    print("Empty definitions for properties")
    find_empty_definitions(properties, modules_names)
    print("-------------------------------------------------------")
    separated_property_definition_df = [
        y for _, y in properties.groupby("Module Name", as_index=True)
    ]
    separated_attribute_definition_df = [
        y for _, y in attributes.groupby("Module Name", as_index=True)
    ]
    # parameters_without_definition = []
    for index, row in mapping.iterrows():
        if row["modules"] in modules_names:
            if row["observable_property_in_protocol"] is not NaN:
                for item in separated_property_definition_df:
                    if item["Module Name"].unique()[0] == row["modules"]:
                        definitions = item
                if (
                    row["observable_property_in_protocol"]
                    not in definitions["Preferred Label"].to_list()
                ):
                    # parameters_without_definition.append(
                    #     "{} : {}".format(
                    #         row[modules], row["observable_property_in_protocol"]
                    #     )
                    # )
                    print(
                        "{} -- {} -- Property : {}".format(
                            index + 2,
                            row["modules"],
                            row["observable_property_in_protocol"],
                        )
                    )
            else:
                for item in separated_attribute_definition_df:
                    if item["Module Name"].unique()[0] == row["modules"]:
                        definitions = item
                if (
                    row["attribute_in_protocol"]
                    not in definitions["Preferred Label"].to_list()
                ):
                    # parameters_without_definition.append(
                    #     "{} : {}".format(row[modules], row["attribute_in_protocol"])
                    # )
                    print(
                        "{} -- {} -- Attribute : {}".format(
                            index + 2, row["modules"], row["attribute_in_protocol"]
                        )
                    )
    # return parameters_without_definition


def get_values(lst, module_name):
    values = []
    for item in lst:
        if item.name == module_name:
            values.extend(
                [
                    item.attribute_collection_uri,
                    item.property_collection_uri,
                    item.method_uri,
                    item.attribute_file_name,
                    item.property_file_name,
                ]
            )
    return values


def get_value_type(str):
    str = str.lower()
    if str == "categorical":
        return "tern:IRI"
    elif str in ["numerical", "numeric"]:
        return "tern:Float"
    elif str in ["number", "percent"]:
        return "tern:Integer"
    elif str in ["alphanumeric", "text", "alphanumerical"]:
        return "tern:Text"
    elif str == "boolean":
        return "tern:Boolean"
    elif str == "datetime":
        return "tern:DateTime"


def generate_categorical_uri(value_type, base_uri, uuid):
    if value_type == "tern:IRI":
        categorical_uri = base_uri + str(uuid).replace(" ", "")
        return categorical_uri
    else:
        return ""


def find_common_parameters(dataframe, modules_names):
    labels = {}
    common_parameters = {}
    for index, row in dataframe.iterrows():
        if row["modules"] in modules_names:
            if row["observable_property_in_protocol"] is not NaN:
                # label = "Property : " + row["observable_property_in_protocol"]
                label = row["observable_property_in_protocol"]
            else:
                # label = "Attribute : " + row["attribute_in_protocol"]
                label = row["attribute_in_protocol"]
            if label in labels:
                labels[label][0] += 1
            else:
                labels[label] = [1, False, ""]
    for key, value in labels.items():
        if value[0] > 1:
            # print(key, "  ", value)
            common_parameters[key] = value
    return common_parameters


# read the data from the spreadsheet

from cmath import nan
import pandas as pd

xls = pd.ExcelFile("spreadsheet.xlsx")
mapping_df = pd.read_excel(xls, "Mapping")
property_df = pd.read_excel(xls, "Observable Properties-definitio")
attribute_df = pd.read_excel(xls, "Attributes - definition")
prefix_df = pd.read_excel(xls, "prefixes")
# print(mapping_df, property_df, attribute_df)

mapping_df = mapping_df.reset_index()
property_df = property_df.reset_index()
attribute_df = attribute_df.reset_index()

# make a list of needed modules and other information
from dawe_vocabs.settings import (
    modules,
    check_inconsistent_names,
    check_incorrect_value_type,
    check_empty_feature_type,
    check_definition,
    check_uuid,
    check_categorical_uuid,
    check_common_parameters,
)

names = []
for i in modules:
    names.append(i.name)

# make sure module names in three files are correct
if check_inconsistent_names:
    check_module_names("Mapping", mapping_df["modules"].unique().tolist(), names)
    check_module_names(
        "Attribute", attribute_df["Module Name"].unique().tolist(), names
    )
    check_module_names("Property", property_df["Module Name"].unique().tolist(), names)

# make sure all the value types are correct
correct_value_types = [
    "categorical",
    "numerical",
    "percentage",
    "number",
    "percent",
    "alphanumeric",
    "alphanumerical",
    "text",
    "boolean",
    "datetime",
    "numeric",
]
if check_incorrect_value_type:
    print(check_value_type(mapping_df, correct_value_types, names))

# make sure all properties has feature types
if check_empty_feature_type:
    print(check_feature_type(mapping_df, names))


# make sure all parameters have definition
if check_definition:
    # check_definition(mapping_df, attribute_df, property_df, names)
    check_parameters_definition(mapping_df, attribute_df, property_df, names)

# make sure all parameters have uuids
if check_uuid:
    print(check_uuids(mapping_df, names))

# make sure all categorical variables have categorical uuids
if check_categorical_uuid:
    print(check_categorical_uuids(mapping_df, names))

# make sure the info for common attributes is the same, like the definition and uuid
if check_common_parameters:
    # print(find_common_parameters(mapping_df, names))
    parameters = []
    for key, value in find_common_parameters(mapping_df, names).items():
        parameters.append(key)
        print(key.lower(), " : ", value)
    print(parameters)

separated_mapping_df = [y for _, y in mapping_df.groupby("modules", as_index=True)]
common_parameters = find_common_parameters(mapping_df, names)


def create_excel_files():
    base_uri = "https://linked.data.gov.au/def/test/dawe-cv/"
    for module in separated_mapping_df:
        module_name = module["modules"].unique()[0]
        if module_name in names:
            module.drop(
                [
                    "Property_type",
                    "comments on categorical variable",
                    "observable_property_tern",
                    "feature_type",
                    "categorical_lut_api_endpoint",
                    "instrument_type",
                    "Notes",
                    "Parameter_created_from_Source",
                ],
                axis=1,
                inplace=True,
            )
            module["definition"] = ""
            module["source"] = ""
            module = module.reset_index()

            definition_list = []
            source_list = []

            for index, row in module.iterrows():
                if row["observable_property_in_protocol"] is NaN:
                    label = row["attribute_in_protocol"]
                    # definition_list.append(
                    #     get_attribute_definition(attribute_df, row["modules"], label)
                    # )
                    # source = attribute_df["Source"].to_list()[
                    #     attribute_df["Preferred Label"].to_list().index(label)
                    # ]
                    print(row["modules"], label)
                    definition, source = get_attribute_definition_source(
                        attribute_df, row["modules"], label
                    )
                    definition_list.append(definition)
                    if (
                        "http://linked.data.gov.au/def/tern-cv/" not in str(source)
                    ) and (
                        "https://linked.data.gov.au/def/test/dawe-cv/"
                        not in str(source)
                    ):

                        source_list.append(source)
                    else:
                        source_list.append(
                            "Ecological Field Monitoring protocols - {}, draft v0.1, 30/11/2021".format(
                                row["modules"].split("-")[0]
                            )
                        )
                else:
                    label = row["observable_property_in_protocol"]
                    # definition_list.append(
                    #     property_df["Definition"].to_list()[
                    #         property_df["Preferred Label"].to_list().index(label)
                    #     ]
                    # )
                    # source = property_df["Source"].to_list()[
                    #     property_df["Preferred Label"].to_list().index(label)
                    # ]
                    print(row["modules"], label)
                    definition, source = get_property_definition_source(
                        property_df, row["modules"], label
                    )
                    definition_list.append(definition)
                    if (
                        "http://linked.data.gov.au/def/tern-cv/" not in str(source)
                    ) and (
                        "https://linked.data.gov.au/def/test/dawe-cv/"
                        not in str(source)
                    ):
                        source_list.append(source)
                    else:
                        source_list.append(
                            "Ecological Field Monitoring protocols - {}, draft v0.1, 30/11/2021".format(
                                row["modules"].split("-")[0]
                            )
                        )
            definition_df = pd.DataFrame(definition_list, columns=["definition"])
            source_df = pd.DataFrame(source_list, columns=["source"])
            module.update(definition_df)
            module.update(source_df)
            # print(module)

            properties_finaldf = []
            attributes_finaldf = []

            (
                attribute_collection_uri,
                property_collection_uri,
                method_uri,
                attribute_file,
                property_file,
            ) = get_values(modules, module_name)

            for index, row in module.iterrows():
                if row["observable_property_in_protocol"] is NaN:
                    # if it is a common attribute
                    if row["attribute_in_protocol"] in common_parameters:
                        # if the attribute has not been created
                        if not common_parameters[row["attribute_in_protocol"]][1]:
                            label = row["attribute_in_protocol"].lower()
                            print(label)
                            attribute_uri = base_uri + str(row["variable_uuid"])
                            value_type = get_value_type(row["value_type"])
                            attributes_finaldf.append(
                                [
                                    attribute_uri,
                                    "skos:Concept",
                                    "",
                                    label,
                                    row["_feature_type"],
                                    value_type,
                                    row["definition"],
                                    generate_categorical_uri(
                                        value_type, base_uri, row["categorical_uuid"]
                                    ),
                                    row["_observable_property_tern"],
                                    "",
                                    row["source"],
                                ]
                            )
                            common_parameters[row["attribute_in_protocol"]][1] = True
                            common_parameters[row["attribute_in_protocol"]][
                                2
                            ] = attribute_uri

                            collection_row = [None] * 11
                            collection_row[0] = attribute_collection_uri
                            collection_row[2] = attribute_uri
                            attributes_finaldf.append(collection_row)
                        # if the attribute has been created, reuse the attribute
                        else:
                            collection_row = [None] * 11
                            collection_row[0] = attribute_collection_uri
                            collection_row[2] = common_parameters[
                                row["attribute_in_protocol"]
                            ][2]
                            attributes_finaldf.append(collection_row)
                    # if it is an unique attribute
                    else:
                        label = row["attribute_in_protocol"].lower()
                        print(label)
                        attribute_uri = base_uri + str(row["variable_uuid"])
                        value_type = get_value_type(row["value_type"])
                        attributes_finaldf.append(
                            [
                                attribute_uri,
                                "skos:Concept",
                                "",
                                label,
                                row["_feature_type"],
                                value_type,
                                row["definition"],
                                generate_categorical_uri(
                                    value_type, base_uri, row["categorical_uuid"]
                                ),
                                row["_observable_property_tern"],
                                "",
                                row["source"],
                            ]
                        )
                        collection_row = [None] * 11
                        collection_row[0] = attribute_collection_uri
                        collection_row[2] = attribute_uri
                        attributes_finaldf.append(collection_row)
                else:
                    # if it is a common property
                    if row["observable_property_in_protocol"] in common_parameters:
                        # if the property has not been created
                        if not common_parameters[
                            row["observable_property_in_protocol"]
                        ][1]:
                            label = row["observable_property_in_protocol"].lower()
                            print(label)
                            property_uri = base_uri + str(row["variable_uuid"])
                            value_type = get_value_type(row["value_type"])
                            properties_finaldf.append(
                                [
                                    property_uri,
                                    "skos:Concept",
                                    "",
                                    label,
                                    row["_feature_type"],
                                    value_type,
                                    generate_categorical_uri(
                                        value_type, base_uri, row["categorical_uuid"]
                                    ),
                                    method_uri,
                                    row["definition"],
                                    row["_observable_property_tern"],
                                    "",
                                    "",
                                    row["source"],
                                ]
                            )
                            common_parameters[row["observable_property_in_protocol"]][
                                1
                            ] = True
                            common_parameters[row["observable_property_in_protocol"]][
                                2
                            ] = property_uri
                            collection_row = [None] * 13
                            collection_row[0] = property_collection_uri
                            collection_row[2] = property_uri
                            properties_finaldf.append(collection_row)
                        else:
                            collection_row = [None] * 13
                            collection_row[0] = property_collection_uri
                            collection_row[2] = common_parameters[
                                row["observable_property_in_protocol"]
                            ][2]
                            properties_finaldf.append(collection_row)
                    # if it is an unique property
                    else:
                        label = row["observable_property_in_protocol"].lower()
                        print(label)
                        property_uri = base_uri + str(row["variable_uuid"])
                        value_type = get_value_type(row["value_type"])
                        properties_finaldf.append(
                            [
                                property_uri,
                                "skos:Concept",
                                "",
                                label,
                                row["_feature_type"],
                                value_type,
                                generate_categorical_uri(
                                    value_type, base_uri, row["categorical_uuid"]
                                ),
                                method_uri,
                                row["definition"],
                                row["_observable_property_tern"],
                                "",
                                "",
                                row["source"],
                            ]
                        )
                        collection_row = [None] * 13
                        collection_row[0] = property_collection_uri
                        collection_row[2] = property_uri
                        properties_finaldf.append(collection_row)

            attributes_finaldf = pd.DataFrame(
                attributes_finaldf,
                columns=[
                    "uri",
                    "rdf:type",
                    "skos:member",
                    "skos:prefLabel",
                    "tern:hasFeatureType",
                    "tern:valueType",
                    "skos:definition",
                    "tern:hasCategoricalCollection",
                    "skos:exactMatch",
                    "skos:closeMatch",
                    "dcterms:source",
                ],
            )
            properties_finaldf = pd.DataFrame(
                properties_finaldf,
                columns=[
                    "uri",
                    "rdf:type",
                    "skos:member",
                    "skos:prefLabel",
                    "tern:hasFeatureType",
                    "tern:valueType",
                    "tern:hasCategoricalCollection",
                    "tern:hasMethod",
                    "skos:definition",
                    "skos:exactMatch",
                    "skos:closeMatch",
                    "skos:example",
                    "dcterms:source",
                ],
            )
            if attribute_file:
                attribute_writer = pd.ExcelWriter(  # pylint: disable=abstract-class-instantiated
                    attribute_file,
                    engine="xlsxwriter",  # pylint: disable=abstract-class-instantiated
                )  # pylint: disable=abstract-class-instantiated
                attributes_finaldf.to_excel(
                    attribute_writer, index=False, sheet_name="sheet1"
                )
                prefix_df.to_excel(attribute_writer, index=False, sheet_name="prefixes")
                attribute_writer.save()
            if property_file:
                property_writer = pd.ExcelWriter(  # pylint: disable=abstract-class-instantiated
                    property_file,
                    engine="xlsxwriter",  # pylint: disable=abstract-class-instantiated
                )  # pylint: disable=abstract-class-instantiated
                properties_finaldf.to_excel(
                    property_writer, index=False, sheet_name="sheet1"
                )
                prefix_df.to_excel(property_writer, index=False, sheet_name="prefixes")
                property_writer.save()


# print(separated_mapping_df[0]["modules"].unique()[0])

create_excel_files()


# print(module)


# basal_area_original_df = pd.DataFrame(
#     columns=[
#         "module_name",
#         "property",
#         "attribute",
#         "categorical_uuid",
#         "value_type",
#         "property_tern",
#         "feature_type",
#     ]
# )
