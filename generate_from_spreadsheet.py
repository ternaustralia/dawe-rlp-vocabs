# download the spreadsheet
# import logging
import pathlib
from re import T
from numpy import NaN
from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth
from oauth2client.service_account import ServiceAccountCredentials
from dawe_vocabs.schemas import ExcelVocab, LUTSchema
import xlsxwriter
from dawe_vocabs import settings


# download the spreadsheet from Google drive
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
    drive_file = drive.CreateFile({"id": file.id})
    drive_file.GetContentFile(
        file.path,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

# check there are no inconsistent module names and syntax errors
def check_module_names(file_name, names_list, modules):
    for i in names_list:
        if i not in modules:
            print(file_name, " -- incorrect module names: ", i)


# check there are no inconsistent module names and syntax errors, replaced by drop down list in the spreadsheet
def check_value_type(dataframe, types: list, modules_names):
    incorrect_value_types = []
    for index, row in dataframe.iterrows():
        if row["modules"] in modules_names:
            if row["value_type_tern"].lower() not in types:
                incorrect_value_types.append(row["value_type_tern"])
    return incorrect_value_types


# make sure all properties have feature types
def check_feature_type(dataframe, modules_names):
    propeties_without_feature_type = []
    for index, row in dataframe.iterrows():
        if row["modules"] in modules_names:
            if row["observable_property_in_protocol"] is not NaN:
                if row["_feature_type"] is NaN:
                    propeties_without_feature_type.append(
                        "{} : {}".format(
                            row["modules"], row["observable_property_in_protocol"]
                        )
                    )
    return propeties_without_feature_type


# make sure all items in `Attributes - definition` and `Observable Properties-definition` have definition
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


# make sure all variables have uuids
def check_uuids(dataframe, modules_names):
    parameters_without_uuids = []
    for index, row in dataframe.iterrows():
        if row["modules"] in modules_names:
            if row["variable_uuid"] is NaN:
                parameters_without_uuids.append(index)
    return parameters_without_uuids


# make sure all categorical parameters have uuids
def check_categorical_uuids(dataframe, modules_names):
    categorical_parameters_without_categorical_uuids = []
    for index, row in dataframe.iterrows():
        if row["modules"] in modules_names:
            if row["value_type_tern"].lower() == "categorical":
                if row["categorical_uuid"] is NaN:
                    categorical_parameters_without_categorical_uuids.append(index)
    return categorical_parameters_without_categorical_uuids


# get the definition and source for attributes from `Attribute - definition`
def get_attribute_definition_source(attributes, module_name, label):
    # separate the dataframe into modules
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


# get the definition and source for properties from `Observable Properties-definition`
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


# make sure each parameter has definition
def check_parameters_definition(mapping, attributes, properties, modules_names):

    # uncomment these prints if want to see parameters with empty definitions
    # print("Empty definitions for attributes")
    # find_empty_definitions(attributes, modules_names)
    # print("-------------------------------------------------------")
    # print("Empty definitions for properties")
    # find_empty_definitions(properties, modules_names)
    # print("-------------------------------------------------------")

    separated_property_definition_df = [
        y for _, y in properties.groupby("Module Name", as_index=True)
    ]
    separated_attribute_definition_df = [
        y for _, y in attributes.groupby("Module Name", as_index=True)
    ]
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
                    print(
                        "{} -- {} -- Attribute : {}".format(
                            index + 2, row["modules"], row["attribute_in_protocol"]
                        )
                    )


# get basic settings for each module, like the uri for attributes collection
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


# get the RDF value type for parameter
def get_value_type(str):
    str = str.lower()
    if str == "categorical":
        return "tern:IRI"
    elif str == "float":
        return "tern:Float"
    elif str == "integer":
        return "tern:Integer"
    elif str == "text":
        return "tern:Text"
    elif str == "boolean":
        return "tern:Boolean"
    elif str == "datetime":
        return "tern:DateTime"
    elif str == "date":
        return "tern:Date"


# create categorical URI
def generate_categorical_uri(value_type, base_uri, uuid):
    if value_type == "tern:IRI":
        categorical_uri = base_uri + str(uuid).replace(" ", "")
        return categorical_uri
    else:
        return ""


# find common parameters in this deliverable
def find_common_parameters(dataframe, modules_names):
    labels = {}
    common_parameters = {}
    for index, row in dataframe.iterrows():
        if row["modules"] in modules_names:
            if row["observable_property_in_protocol"] is not NaN:
                label = row["observable_property_in_protocol"]
            else:
                label = row["attribute_in_protocol"]
            # count the times for each parameter
            if label in labels:
                labels[label][0] += 1
            else:
                # number means times of appearance; boolean value means whether this parameter is created in vocabulary; the last value is variable uuid
                labels[label] = [1, False, ""]
    for key, value in labels.items():
        if value[0] > 1:
            common_parameters[key] = value
    return common_parameters


# TODO: this function has one extra condition, could be integrated with the above one
def find_common_categorical_parameters(dataframe, modules_names):
    labels = {}
    common_parameters = {}
    for index, row in dataframe.iterrows():
        if (row["modules"] in modules_names) and (
            row["value_type_tern"].lower() == "categorical"
        ):
            if row["observable_property_in_protocol"] is not NaN:
                label = row["observable_property_in_protocol"]
            else:
                label = row["attribute_in_protocol"]
            if label in labels:
                labels[label][0] += 1
            else:
                labels[label] = [1, False, ""]
    for key, value in labels.items():
        if value[0] > 1:
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

mapping_df = mapping_df.reset_index()
property_df = property_df.reset_index()
attribute_df = attribute_df.reset_index()

# needed info from settings.py
from dawe_vocabs.settings import (
    modules,
    correct_value_types,
    check_inconsistent_names,
    check_incorrect_value_type,
    check_empty_feature_type,
    check_definition,
    check_uuid,
    check_categorical_uuid,
    check_common_parameters,
    generate_vocabs,
    check_common_categorical_parameters,
)

# put all module names in one list, for later use
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

# make sure all value types are correct
if check_incorrect_value_type:
    print(check_value_type(mapping_df, correct_value_types, names))

# make sure all properties has feature types
if check_empty_feature_type:
    print(check_feature_type(mapping_df, names))

# make sure all parameters have definition
if check_definition:
    check_parameters_definition(mapping_df, attribute_df, property_df, names)

# make sure all parameters have uuids
if check_uuid:
    print(check_uuids(mapping_df, names))

# make sure all categorical variables have categorical uuids
if check_categorical_uuid:
    print(check_categorical_uuids(mapping_df, names))

# make sure the info for common attributes is the same, like the definition and uuid
if check_common_parameters:
    parameters = []
    for key, value in find_common_parameters(mapping_df, names).items():
        parameters.append(key.lower())
        print(key.lower(), " : ", value)
    print(parameters)

# find all common categorical parameters
if check_common_categorical_parameters:
    parameters = []
    for key, value in find_common_categorical_parameters(mapping_df, names).items():
        parameters.append(key.lower())
        print(key.lower(), " : ", value)
    print(parameters)

separated_mapping_df = [y for _, y in mapping_df.groupby("modules", as_index=True)]
common_parameters = find_common_parameters(mapping_df, names)


def create_excel_files():
    base_uri = "https://linked.data.gov.au/def/test/dawe-cv/"
    # loop through each module or submodule
    for module in separated_mapping_df:
        module_name = module["modules"].unique()[0]
        if module_name in names:
            # these columns are not used
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
            # create definition and source column
            module["definition"] = ""
            module["source"] = ""
            module = module.reset_index()

            # create definition and source list, to be added in those 2 new columns
            definition_list = []
            source_list = []

            # loop through each row (each parameter) in current module, and get the definition, source for each parameter
            for index, row in module.iterrows():
                if row["observable_property_in_protocol"] is NaN:
                    label = row["attribute_in_protocol"]
                    print(row["modules"], label)  # to see the generating process

                    # add the parameter definition to definition list
                    definition, source = get_attribute_definition_source(
                        attribute_df, row["modules"], label
                    )
                    definition_list.append(definition)

                    # if the source is from book, essay and other acadmeic sources
                    if (
                        "http://linked.data.gov.au/def/tern-cv/" not in str(source)
                    ) and (
                        "https://linked.data.gov.au/def/test/dawe-cv/"
                        not in str(source)
                    ):
                        source_list.append(source)
                    # if the source is from GraphDB only, not meaningful enough, add the protocol file as reference
                    else:
                        source_list.append(
                            "Ecological Field Monitoring protocols - {}, draft v0.1, 30/11/2021".format(
                                row["modules"].split("-")[0]
                            )
                        )
                # when parameter is property
                else:
                    label = row["observable_property_in_protocol"]
                    print(row["modules"], label)  # to show generating process

                    # TODO: it is similar to adding attribute definition
                    definition, source = get_property_definition_source(
                        property_df, row["modules"], label
                    )
                    definition_list.append(definition)

                    # TODO: similar to add attribute source
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

            # convert definition and source list to pandas dataframes, and put them in the dataframe for this module or submodule
            definition_df = pd.DataFrame(definition_list, columns=["definition"])
            source_df = pd.DataFrame(source_list, columns=["source"])
            module.update(definition_df)
            module.update(source_df)

            # create 2 empty dataframes for properties and attributes, for this module or submodule
            properties_finaldf = []
            attributes_finaldf = []

            # get the basic settings for each parameter
            # `attribute_file` is the file path to create attributes excel file, similar for `property_file`
            (
                attribute_collection_uri,
                property_collection_uri,
                method_uri,
                attribute_file,
                property_file,
            ) = get_values(modules, module_name)

            # start creating excel files, now the dataframe `module` contains all info needed to create vocabulary
            for index, row in module.iterrows():
                # if the parameter is an attribute
                if (
                    (row["observable_property_in_protocol"] is NaN)
                    and (row["attribute_in_protocol"] is not NaN)
                    and (
                        str(row["attribute_in_protocol"])
                        not in settings.deleted_parameters
                    )
                ):
                    # if it is a common attribute
                    if row["attribute_in_protocol"] in common_parameters:
                        # if the attribute has not been created, checked by a boolean variable
                        if not common_parameters[row["attribute_in_protocol"]][1]:
                            label = row["attribute_in_protocol"].lower()
                            print(label)  # to see the generating process
                            attribute_uri = base_uri + str(row["variable_uuid"])
                            value_type = get_value_type(row["value_type_tern"])
                            # add the information for this parameter
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
                            # change the boolean value to indicate this common parameter is created
                            common_parameters[row["attribute_in_protocol"]][1] = True
                            # record the common parameter uri
                            common_parameters[row["attribute_in_protocol"]][
                                2
                            ] = attribute_uri

                            # add the collection row, with the collection uri and the parameter uri
                            collection_row = [None] * 11
                            collection_row[0] = attribute_collection_uri
                            collection_row[2] = attribute_uri
                            attributes_finaldf.append(collection_row)
                        # if the attribute has been created, reuse the attribute uri directly in the collection row
                        else:
                            collection_row = [None] * 11
                            collection_row[0] = attribute_collection_uri
                            collection_row[2] = common_parameters[
                                row["attribute_in_protocol"]
                            ][2]
                            attributes_finaldf.append(collection_row)
                    # if it is an unique attribute
                    # TODO: this process is the same as the above to create the common parameter, should be integrated
                    else:
                        label = row["attribute_in_protocol"].lower()
                        print(label)
                        attribute_uri = base_uri + str(row["variable_uuid"])
                        value_type = get_value_type(row["value_type_tern"])
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
                # if the paramter is a property
                elif (row["observable_property_in_protocol"] is not NaN) and (
                    str(row["observable_property_in_protocol"])
                    not in settings.deleted_parameters
                ):
                    # if it is a common property
                    if row["observable_property_in_protocol"] in common_parameters:
                        # if the property has not been created
                        if not common_parameters[
                            row["observable_property_in_protocol"]
                        ][1]:
                            label = row["observable_property_in_protocol"].lower()
                            print(label)
                            property_uri = base_uri + str(row["variable_uuid"])
                            value_type = get_value_type(row["value_type_tern"])
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
                    # TODO: same as the above to create the common property, should be integrated
                    else:
                        label = row["observable_property_in_protocol"].lower()
                        print(label)
                        property_uri = base_uri + str(row["variable_uuid"])
                        value_type = get_value_type(row["value_type_tern"])
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

            # add column names for the dataframe, attribute is different from property
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
            # if the attribute file path is given, generate the attributes excel file for this module
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
            # if the property file path is given, generate the properties excel file for this module
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


# uncomment this print to see the current generating module, may not be useful because the printing for each parameter
# print(separated_mapping_df[0]["modules"].unique()[0])

if generate_vocabs:
    create_excel_files()

# uncomment this print to see the module dataframe
# print(module)
