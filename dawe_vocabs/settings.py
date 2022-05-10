from dawe_vocabs.schemas import LUTSchema, ExcelVocab, InfoNeeded

from typing import List

from rdflib import Namespace

# Settings

# Show table result in logging output.
show_table_result = True

# Download Excel files from Google Drive.
download_excel_files = True

# Base URI used for all generated vocabularies.
base_uri = Namespace("https://linked.data.gov.au/def/test/dawe-cv/")

# SHACL shapes file.
shapes_file = "shapes.shapes.ttl"

# Parent categorical values collection
parent_collection_uri = (
    "https://linked.data.gov.au/def/test/dawe-cv/05f83f99-1998-4d11-8837-bb4a68788521"
)

# Look up tables to be generated.
lut_configs: List[LUTSchema] = [
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-tier-2-observation-methods",
        "Observation method tier 2 codes",
        "A collection of observation tier 2 types and its codes.",
        "f1592e71-cc16-4b81-90c4-06b418a5a766",
        "observation method tier 2",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fauna-vagina-conditions",
        "Vaginal condition codes",
        "A collection of vaginal condition types and its codes.",
        "09de3b86-616e-49af-a34c-903cf7dec443",
        "vaginal condition",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-voucher-types",
        "Voucher type codes",
        "A collection of voucher types and its codes.",
        "a3333793-95bd-47fc-ba90-b8fc65a40456",
        "voucher type",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fauna-behaviours",
        "animal behaviour codes",
        "A collection of animal behaviour types and its codes.",
        "1301857c-4e02-4000-966b-a0d0ce60368f",
        "animal behaviour",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-habitats",
        "Habitat description codes",
        "A collection of habitat description types and its codes.",
        "c19a0098-1f3f-4bc2-b84d-fdb6d4e24d6f",
        "habitat description",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-tier-1-observation-methods",
        "Observation method tier 1 codes",
        "A collection of observation tier 1 types and its codes.",
        "6b6ec6a4-33d2-4515-b988-617d190cfbdb",
        "observation method tier 1",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-substratum-types",
        "Substratum type codes",
        "A collection of substratum types and its codes.",
        "7fc2cae5-74f6-426d-a25d-cbf9423b572a",
        "substratum type",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-stratum-types",
        "Stratum type codes",
        "A collection of stratum types and its codes.",
        "eb6e9a4c-e277-4cb3-9792-9c91311b7e03",
        "stratum type",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-voucher-conditions",
        "Voucher condition codes",
        "A collection of voucher condition types and its codes.",
        "600aa845-fe4d-4891-bf39-2e56220022cc",
        "voucher condition",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-preservation-types",
        "Preservation type codes",
        "A collection of preservation types and its codes.",
        "4e5037f1-97e6-4866-a018-915bcf482261",
        "preservation type",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-tier-2-microhabitats",
        "Microhabitat tier 2 codes",
        "A collection of microhabitat tier 2 types and its codes.",
        "48f0bb5d-5451-42a1-ad60-7ddca485412d",
        "microhabitat tier 2",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-tier-1-microhabitats",
        "Microhabitat tier 1 codes",
        "A collection of microhabitat tier 1 types and its codes.",
        "66034d49-50d7-4042-a252-c2bd249d2a4b",
        "microhabitat tier 1",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-vegetation-types",
        "Vegetation type codes",
        "A collection of vegetation types and its codes.",
        "2f585fb4-996c-483c-9f9f-65e5bbd171b3",
        "vegetation type",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fauna-breeding-codes",
        "Breeding status codes",
        "A collection of breeding status types and its codes.",
        "b7dc10d2-c0aa-46b3-94da-685cd0a723e4",
        "breeding status",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fauna-age-classes",
        "Age class codes",
        "A collection of age class types and its codes.",
        "0e2641c3-0d7e-4d94-8cd7-02c21d564630",
        "age class",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-phenologies",
        "Phenology codes",
        "A colleciton of phenology types and its codes",
        "110398ca-32fa-4f69-b7bb-5aa69d5a5004",
        "phenology type",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fauna-pouch-conditions",
        "Animal pouch condition codes",
        "A collection of animal pouch condition types and its codes.",
        "4fab0c1c-c127-474e-8f5e-4afe45fec0ed",
        "animal pouch condition",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fauna-teats-conditions",
        "Animal teats condition codes",
        "A collection of animal teats condition types and its codes.",
        "d2665d51-db1d-48ad-a80d-48593d280b76",
        "animal teats condition",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fauna-testes-conditions",
        "Animal testes condition codes",
        "A collection of animal testes condition types and its codes.",
        "c5d3877d-1a83-4a87-9bdd-05f77c516df6",
        "animal testes condition",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fauna-sexes",
        "Animal sex codes",
        "A collection of animal sex types and its codes.",
        "fcc3a1e1-3e35-4a4f-bd44-eface035025c",
        "animal sex",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-specimen-locations",
        "Specimen location codes",
        "A collection of specimen location types and its codes.",
        "1df5afd1-475a-435a-94c5-143b707aab10",
        "specimen location",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-identification-methods",
        "Method of identification codes",
        "A collection of method of identification types and its codes.",
        "43c7a4be-72f3-4007-9777-7e7aa2d8da25",
        "method of identification",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-identification-sources",
        "Source of identification codes",
        "A collection of source of identification types and its codes.",
        "a36600ac-b9ed-44d1-b199-85ee1d802e58",
        "source of identification",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-taxa-types",
        "Taxa type codes",
        "A collection of taxa types and its codes.",
        "7ea12fed-6b87-4c20-9ab4-600b32ce15ec",
        "taxa type",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-cover-codes",
        "Cover class codes",
        "A collection of cover class types and its codes.",
        "6aaa330c-3d60-419b-a29b-a2dbc6d67928",
        "cover class",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-landform-patterns",
        "Landform pattern codes",
        "A collection of landform pattern types and its codes.",
        "19d91a7a-2733-4b84-9d2b-4bda4808c003",
        "landform pattern",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-landform-elements",
        "Landform element codes",
        "A collection of landform element types and its codes.",
        "c1a58967-cb12-4c2c-a7ca-9cee2589919c",
        "landform element",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-plot-slopes",
        "Plot slope codes",
        "A collection of plot slope types and its codes.",
        "d893e669-c530-4bc3-a057-a5799ffcb5db",
        "plot slope",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-soils-surface-strew-sizes",
        "Soil surface strew size codes",
        "A collection of soil surface strew size types and its codes.",
        "3b25ce0f-9eb7-4d2d-97ce-143858cfd4d4",
        "soil surface strew size",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-soils-lithologies",
        "Soil lithology codes",
        "A collection of soil lithology types and its codes.",
        "1d50eb79-685f-45ea-84b4-627154eddede",
        "soil lithology",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-veg-structural-formations",
        "Vegetation structural formation codes",
        "A collection of vegetation structural formation types and its codes.",
        "6e9baf51-566e-4a5d-93c4-a6e097dc364d",
        "vegetation structural formation",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-climatic-conditions",
        "Climatic condition codes",
        "A collection of climatic condition types and its codes.",
        "2ebfee89-92db-44b3-bb89-06dd92798ae6",
        "climatic condition",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-veg-growth-stages",
        "Vegetation growth stage codes",
        "A collection of vegetation growth stage types and its codes.",
        "89c02383-fb5e-4acd-b248-902a2d579170",
        "vegetation growth stage",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fire-histories",
        "Fire history codes",
        "A collection of fire history types and its codes.",
        "6e9d2f51-ce64-4c67-8391-d14a8bf96b6b",
        "fire history",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-disturbances",
        "Disturbance type codes",
        "A collection of disturbance types and its codes.",
        "f5a470e8-d29f-4ff6-b50d-529b0444dbe4",
        "disturbance type",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-veg-growth-forms",
        "Vegetation growth form codes",
        "A collection of vegetation growth form types and its codes.",
        "d0fc07a7-3ec9-45ed-8850-885a32828d3c",
        "vegetation growth form",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-veg-height-classes",
        "Vegetation height class codes",
        "A collection of vegetation height class types and its codes.",
        "b1b05cd1-3b85-4639-a6af-799a34d88d43",
        "vegetation height class",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-soils-substrates",
        "Soil substrate codes",
        "A collection of soil substrate types and its codes.",
        "b061d7db-a608-4062-96d4-b367d6d9a792",
        "soil substrate",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-basal-tree-trunk-types",
        "Basal tree trunk types",
        "A collection of basal tree trunk types and its codes.",
        "9282400b-56c3-49a9-bb82-87ef74914690",
        "Basal tree trunk",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-basal-tree-statuses",
        "Basal tree statuses",
        "A collection of basal tree statuses and its codes.",
        "f06740e7-2857-415a-a6dc-72dbbba7a88c",
        "Basal tree status",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-basal-area-factors",
        "Basal area factors",
        "A collection of basal area factors and its codes.",
        "13d010d7-91b7-4621-b80a-70cb4324ddf5",
        "Basal area factors",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-basal-sweep-sampling-points",
        "Basal sweep sampling points codes",
        "A collection of basal sweep sampling points and its codes.",
        "96d41885-70e5-44c1-bafc-73027f47941b",
        "basal sweep sampling points",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-cwd-sampling-survey-methods",
        "Coarse Woody Debris sampling survey methods codes",
        "A collection of Coarse Woody Debris sampling survey methods and its codes.",
        "bd41602d-36df-435c-870c-496dfd523ec1",
        "Coarse Woody Debris sampling survey methods",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-cwd-transect-numbers",
        "Coarse Woody Debris transect numbers codes",
        "A collection of Coarse Woody Debris transect numbers and its codes.",
        "c117bd06-9603-400d-a20d-29f56ffa78cc",
        "Coarse Woody Debris transect numbers",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-cwd-decay-classes",
        "Coarse Woody Debris decay classes codes",
        "A collection of Coarse Woody Debris decay classes and its codes.",
        "b5180d8a-75b6-4bca-9413-0e507e910387",
        "Coarse Woody Debris decay classes",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-condition-growth-stage-trees",
        "Condition growth stage trees codes",
        "A collection of condition growth stage trees and its codes.",
        "8af52d41-016c-4d53-85ca-2357c3a1468d",
        "Condition growth stage trees",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-condition-growth-stage-shrubs",
        "Condition growth stage shrubs codes",
        "A collection of condition growth stage shrubs and its codes.",
        "b7066d4c-2d7b-4c1b-a8f2-401fd243ac3f",
        "Condition growth stage shrubs",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-condition-life-stages",
        "Condition life stages codes",
        "A collection of condition life stages and its codes.",
        "5f82c583-167b-4ed2-b25e-4d67decb3f2d",
        "Condition life stages",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-condition-vegetation-diameter-classes",
        "Condition vegetation diameter classes codes",
        "A collection of condition vegetation diameter classes and its codes.",
        "fe0b8990-dc4c-4fc7-85e8-be08da5721a0",
        "Condition vegetation diameter",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-condition-vertebrate-pest-types",
        "Condition vertebrate pest types codes",
        "A collection of condition vertebrate pest types and its codes.",
        "1eaaabf9-57a9-4c95-9cf3-58c20263b2a0",
        "Condition vertebrate pest",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fire-plot-burned-statuses",
        "Fire plot burned statuses codes",
        "A collection of fire plot burned statuses and its codes.",
        "5662a7dd-c1da-4659-8290-a1e6e42c879f",
        "Fire plot burned statuses",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fire-substrate-types",
        "Fire substrate types codes",
        "A collection of fire substrate types and its codes.",
        "0b89087f-345a-4e8d-8f84-38d5af499f10",
        "Fire substrate",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fire-growth-forms",
        "Fire growth forms codes",
        "A collection of fire growth forms and its codes.",
        "032ed6fa-4c55-4752-b625-3e6b32672444",
        "Fire growth forms",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fire-species",
        "Fire species codes",
        "A collection of fire species forms and its codes.",
        "e02a2654-206b-4f15-9132-166321efd122",
        "Fire species",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fire-regeneration-statuses",
        "Fire regeneration statuses codes",
        "A collection of fire regeneration statuses and its codes.",
        "a1b8fc00-5d5f-40f8-a7e1-0b09d4bbba4b",
        "Fire regeneration statuses",
    ),
    LUTSchema(
        "https://dev.core-api.paratoo.tern.org.au/lut-fire-plant-alive-statuses",
        "Fire plant alive statuses codes",
        "A collection of fire plant alive statuses and its codes.",
        "29d1081d-9cde-42ab-b59a-6bfc8bdda01d",
        "Fire plant alive statuses",
    ),
]

# Excel files to be generated using excel2rdf.
excel_files_dir_first = "vocab-sources/first-stage"
excel_files_dir_second = "vocab-sources/second-stage"

excel_files = (
    ExcelVocab(
        "vocab-sources/first-stage/register.xlsx", "1YBOPh7SZpKS-qDxN_Tl-uuZ4slLMbLjD"
    ),
    ExcelVocab(
        "vocab-sources/first-stage/categorical-values-collection.xlsx",
        "1KPEq5JiqJhQyTp0oihVNhHbLkyhMLG_R",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/protocols-collection.xlsx",
        "1RLOQvSXfLaJ-eRSfWa6KPDXTn4a_MRNA",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/protocols-plot-selection.xlsx",
        "1S_Cx42safRFWOa0iSDdDDdULP1fRlpSh",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/observable-properties-by-module.xlsx",
        "1kzR1BTPgARnWfHh_mK-xx15TEl1D2bky",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/protocols-plot-description.xlsx",
        "1Dbrhl1gTIMn7VaijCiSbQc63ybpQmXd_",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/plot-description-observable-properties-collection.xlsx",
        "1qPJ3I4NhfnKLDiqBQVkolAYBDbSZEPQ7",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/plot-description-observable-properties.xlsx",
        "1wmEWPnAmo2kunMH_zLSq3HkXckY8Ml33",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/protocols-cover.xlsx",
        "11OD9vTq8TDCOyHmOZHutWr-1dK6t7Zsv",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/cover-observable-properties-collection.xlsx",
        "1jUcXQ1HQ9RxxJeYxWp7dosjdwFr0vVw2",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/cover-observable-properties.xlsx",
        "1nw2KeprNMmIYYzHz_T2-bD3IoSyj2ayb",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/protocols-floristics.xlsx",
        "1BryGRR1JYl_2eLisqrF9SZyw7ZnRj-Ix",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/floristics-observable-properties-collection.xlsx",
        "1tWaBUfSol735NzpPeTTpYIpkNE9JaIzJ",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/floristics-observable-properties.xlsx",
        "1gsS0NgpF1Njs-S4hW0rSTQJbpi-N7oEl",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/protocols-plant-tissue-vouchering.xlsx",
        "19ghAUOE0GGFw5UDxmEyOtFJRgmVy6XRO",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/protocols-vegetation-mapping.xlsx",
        "1Ofkweb9pNvMT4OT53P7NNh-v4FevjbTs",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/vegetation-mapping-observable-properties-collection.xlsx",
        "1OnomiXiDzHhTNrM5p1xINguiP5tPrydF",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/vegetation-mapping-observable-properties.xlsx",
        "1BiWiCK0O3OZPfsyUBIhdx0HyFTb-Xy-S",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/protocols-opportunistic-observations.xlsx",
        "1dTfOpJ9l68qVs9msUWQVDfilWExG_NkW",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/opportunistic-observations-observable-properties-collection.xlsx",
        "15KybrSynrOW26eDFy9ZxQzR4BdYTtz_N",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/opportunistic-observations-observable-properties.xlsx",
        "1AMWD4_SZQBbut4MxYqJPE8IvxdJFMzkJ",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/protocols-photopoints.xlsx",
        "1cei9yda7SRMSdDD9VRL-DAGTbHJhSXEZ",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/attributes-by-module.xlsx",
        "1BIrNDeyaLpeBHz3_Q9y0G_ia0aB60hWQ",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/plot-description-attributes-collection.xlsx",
        "1WdPNWuukZhtfOXGOe1Tk_bJBuL9HhgDS",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/plot-description-attributes.xlsx",
        "15ghEl_ntzXM-A7N7xtOWkPOnFxQWJTPa",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/plot-selection-attributes-collection.xlsx",
        "12LZSkM_4n_wsb4dIlm1B3tf6W_iNXqVx",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/plot-selection-attributes.xlsx",
        "1BersV0IrGl-LVeuiQfZr5HAFNGphv0Vu",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/opportunistic-observations-attributes-collection.xlsx",
        "1gZdZgQw4RdYbOT87QXqABydcJfZYY50X",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/opportunistic-observations-attributes.xlsx",
        "12g7ERev4ZWOY4PPRrSPM2N8rEmndW6-g",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/photopoints-attributes-collection",
        "1Jk-YICjZFBVM8P7zugj9HdtGI_35LOj3",
    ),
    ExcelVocab(
        "vocab-sources/first-stage/photopoints-attributes.xlsx",
        "100lA3JvWQXugH3o7qPbIlA_-KeFzJmoq",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/basal-area-attributes-collection.xlsx",
        "1-4jcmg-ly2waMRVAvsIEFqBThaggTlh9",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/basal-area-attributes.xlsx",
    #     "1XlrN9Lf2s5DPxOBLu4oMmvk8efBOtSGl",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/basal-area-properties-collection.xlsx",
        "12u4WnYitHLDuYDECSmqyxhRexYUvcFqR",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/basal-area-properties.xlsx",
    #     "1nuRUsQzXz6K7lmzAMTTJ_cmYVh1LRLt0",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/coarse-woody-debris-attributes-collection.xlsx",
        "17qCVHfj7Aio3BKhiLiIKZQAava2ceWSx",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/coarse-woody-debris-attributes.xlsx",
    #     "1e-FZklwVaSt8n-WA24vq54aOl-gznFMH",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/coarse-woody-debris-properties-collection.xlsx",
        "1E6oBGu-lcqpjCir99kDeZ5HyKxvKUBvg",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/coarse-woody-debris-properties.xlsx",
    #     "1FYsYuozWG9IFYUR6xNqpnV1vL6tW2oXh",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/condition-attributes-collection.xlsx",
        "1Izsg_5cBqJVyeLIwiY32ZzUTi1AHlgTc",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/condition-attributes.xlsx",
    #     "1BEi6UAYVqL1WR5rtBW4oBXlvYuCGaMEm",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/condition-properties-collection.xlsx",
        "1YP4Gm58oQ3Vdg_Uupszyif4NOQXoSIF4",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/condition-properties.xlsx",
    #     "1_n1W68h7-wzsqFx6mLws46rG3y5sXD7V",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/fire-attributes-collection.xlsx",
        "1KMQNMZKWvYALgXkZqipRE0M-gZtG4KrR",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/fire-attributes.xlsx",
    #     "1Vf0H8D8_G27G25SfgZJFGjG08p-NhPxD",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/fire-properties-collection.xlsx",
        "1DPHQmvCZl2pp1Ve4DyQIRVJQGGmQvajU",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/fire-properties.xlsx",
    #     "1i_eHyoP6P1IQdqAMe9UPyrxyMD-1aqdh",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-basal-area-overview.xlsx",
        "1bPLqIkhSncMsEoA8SWcm-v9iuL8Nxyqs",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-basal-area.xlsx",
        "17napKRwRmuDu4Mrn-eeGo0RsjOc2R5th",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/soil-attributes-collection.xlsx",
        "1N41LV3utkikRP9Zqogh_lUGLM0ory0ag",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/soil-attributes-collection-with-submodules.xlsx",
        "1dspAnx-DTrYCtZ8wKvy-LhGy_x1OVWtj",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/soil-properties-collection.xlsx",
        "1ip12rjYBRMCMKSSV5pmnxYhHcoZziZuw",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/soil-properties-collection-with-submodules.xlsx",
        "1l0fWiSToDVsc1jYQMVsfQQDQLdkAXik8",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/soil-plot-soil-description-properties.xlsx",
    #     "1Olb85Vaz0Rl4pu93tOX43uadkxQf3m1o",
    # ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/soil-plot-soil-description-attributes.xlsx",
    #     "1uhENUBGOEaIePjvZf-y-rCuWtoPrN_pd",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/soil-attributes-collection-general.xlsx",
        "1W_cxmBQgn96rjKYhnB-levBBHZu8Audk",
    ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/soil-soil-pit-characterization-attributes.xlsx",
    #     "1tIk6Rvy8skpthNdc6HD8Ll6meWqCacmL",
    # ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/soil-soil-pit-characterization-properties.xlsx",
    #     "1_wFq3kCNb7Q_7Nz26xXhavILwbu1zf1A",
    # ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/soil-soil-subsite-sampling-attributes.xlsx",
    #     "1oaSSog-9TaqX7Lz883s_mPRnEtgLJ0jm",
    # ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/soil-soil-subsite-sampling-properties.xlsx",
    #     "1W7j-mjWPhvM-MukCa7eFWoeEFWJkQjGm",
    # ),
    # ExcelVocab(
    #     "vocab-sources/second-stage/soil-soil-bulk-density-properties.xlsx",
    #     "1l8oaY8hQ931U1GjOUMjGwNRn_upi3QPl",
    # ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-cwd-overview.xlsx",
        "1znaJv6W5XXP2xlAv5v21GUkQpn1j70Ak",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-cwd.xlsx",
        "1i04_Aj2XvfXVkCnUnd_MMqwTBFk4p9Vc",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-condition-overview.xlsx",
        "1cxOhPWnSq8gJ_H_KLLSSnsAp6b-StUDk",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-condition.xlsx",
        "1ViFC0dM3ZvSuzt8bWZ7HKBrBz79igxg6",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/invertebrate-attributes-collection.xlsx",
        "1YmX2cwGg16kGD_V4GEBGirJ7vDp5cea-",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/invertebrate-attributes-with-submodules.xlsx",
        "1g49wyzAnqWfe7MuqHOlPN7SO03WRiaGP",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/invertebrate-properties-collection.xlsx",
        "1VQLH6UPkX4ec1vkiYozvS7HRhAhf5ThK",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/invertebrate-properties-with-submodules.xlsx",
        "1lhv7ZWMpxJVrTBJ68smTPuP3QjKrJPiy",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-fire.xlsx",
        "1miU_TIYLQwzn0a4jrrNfi5FZKaD0uFB0",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-soil-overview.xlsx",
        "1BFn_n95_W6QFi4LEPpm9KMNH5wTiBqjG",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-soil.xlsx",
        "1CYnpGNFl-fDO3T_jKZXRAG2RkIM1VMqM",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-invertebrate-overview.xlsx",
        "12HD6BRbBZXz7fWEog0lzUvd-6eiuN8HF",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/protocols-invertebrate.xlsx",
        "1LNQqsUWPd6QB9WgnRDqG3EQuHq_GwwVa",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/targeted-survey-properties-collection.xlsx",
        "1RU1GpcpBnrXvPgXrknp75I40Z3y8LIv2",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/targeted-survey-attributes-collection.xlsx",
        "1zm15h_Z1zldyLkMAUfh7bzSH8HReWuk0",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/targeted-survey-properties-collection-with-submodules.xlsx",
        "1ry8DQ0et1lsD5M5de6W-iuJj8s3w26-s",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/targeted-survey-attributes-collection-with-submodules.xlsx",
        "1yMPBHT2dGqATlbQnFwfTGK6tK1IoiiGX",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/targeted-survey-fauna-properties-collection-with-submodules.xlsx",
        "10amCfN7wKDh8NJYdXDjZTcIU17gMOxgv",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/targeted-survey-fauna-attributes-collection-with-submodules.xlsx",
        "1tkW_JvHCFKifrg4CtR0RC7J6P0ylqk3S",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/targeted-survey-flora-properties-collection-with-submodules.xlsx",
        "1LCF8J_rqfopofbCUkTGAKlbYl0Hj_RVA",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/targeted-survey-flora-attributes-collection-with-submodules.xlsx",
        "1QOfT5nsdoNmLauSeYGpItrcWLCVYOj5P",
    ),
)

check_inconsistent_names = False
check_incorrect_value_type = False
check_empty_feature_type = False
check_definition = False
check_uuid = False
check_categorical_uuid = False
check_common_parameters = False

modules = [
    InfoNeeded(
        "Basal area module",
        "https://linked.data.gov.au/def/test/dawe-cv/2c11309d-b846-4a40-a571-6af773d380c6",
        "https://linked.data.gov.au/def/test/dawe-cv/ab7c4569-312c-4450-b413-9b11c4d2577b",
        "https://linked.data.gov.au/def/test/dawe-cv/f7e0d965-ae73-434e-8599-634598e506b5",
        "vocab-sources/second-stage/basal-area-attributes.xlsx",
        "vocab-sources/second-stage/basal-area-properties.xlsx",
    ),
    InfoNeeded(
        "Coarse Woody Debris module",
        "https://linked.data.gov.au/def/test/dawe-cv/5bee1509-b8fc-452e-9a06-0aa03d8f196f",
        "https://linked.data.gov.au/def/test/dawe-cv/3a17f41f-1cf2-4abb-bde1-3b9a1388051e",
        "https://linked.data.gov.au/def/test/dawe-cv/f455e72b-8fad-4d5d-8dfc-3f1464e91a6e",
        "vocab-sources/second-stage/coarse-woody-debris-attributes.xlsx",
        "vocab-sources/second-stage/coarse-woody-debris-properties.xlsx",
    ),
    InfoNeeded(
        "Condition Module",
        "https://linked.data.gov.au/def/test/dawe-cv/ce3412d6-a99e-482c-9651-5b2b5ac42456",
        "https://linked.data.gov.au/def/test/dawe-cv/1d6ca60e-4371-4248-a383-5d4bd4d88c65",
        "https://linked.data.gov.au/def/test/dawe-cv/16a20c3f-e95d-4919-b2d1-a25c7a275109",
        "vocab-sources/second-stage/condition-attributes.xlsx",
        "vocab-sources/second-stage/condition-properties.xlsx",
    ),
    InfoNeeded(
        "Fire Module",
        "https://linked.data.gov.au/def/test/dawe-cv/e8f2ee06-9943-49a4-b113-064f8e195dca",
        "https://linked.data.gov.au/def/test/dawe-cv/75002e1e-7866-4264-9e20-8569743ea4f5",
        "https://linked.data.gov.au/def/test/dawe-cv/a8da406b-22bf-444b-a3ea-ccf62130d6f6",
        "vocab-sources/second-stage/fire-attributes.xlsx",
        "vocab-sources/second-stage/fire-properties.xlsx",
    ),
    InfoNeeded(
        "Soil module - Plot soil description protocol",
        "https://linked.data.gov.au/def/test/dawe-cv/16a1a45f-b4a4-4eef-af45-2b72477a4178",
        "https://linked.data.gov.au/def/test/dawe-cv/5b7addb7-ae3d-47eb-b5d8-f34cc211875a",
        "https://linked.data.gov.au/def/test/dawe-cv/7818e122-6354-42e0-aeff-32dbab7baae4",
        "vocab-sources/second-stage/soil-plot-soil-description-attributes.xlsx",
        "vocab-sources/second-stage/soil-plot-soil-description-properties.xlsx",
    ),
    InfoNeeded(
        "Soil module - soil pit characterization protocol",
        "https://linked.data.gov.au/def/test/dawe-cv/461223ed-8855-4c1b-b24c-aa078ffb402b",
        "https://linked.data.gov.au/def/test/dawe-cv/760751fb-7a1b-4874-9de6-98127febac58",
        "https://linked.data.gov.au/def/test/dawe-cv/8f00b7c6-34b4-4203-8dcc-4be47f21d7db",
        "vocab-sources/second-stage/soil-soil-pit-characterization-attributes.xlsx",
        "vocab-sources/second-stage/soil-soil-pit-characterization-properties.xlsx",
    ),
    InfoNeeded(
        "Soil module - soil subsite sampling protocol",
        "https://linked.data.gov.au/def/test/dawe-cv/8981bb19-3158-48ed-9a91-aae67e358256",
        "https://linked.data.gov.au/def/test/dawe-cv/eaf5a55e-e053-4818-a808-4722b1da4d17",
        "https://linked.data.gov.au/def/test/dawe-cv/e3ad3e5b-7c1c-4b59-bdb1-297f707d2ca3",
        "vocab-sources/second-stage/soil-soil-subsite-sampling-attributes.xlsx",
        "vocab-sources/second-stage/soil-soil-subsite-sampling-properties.xlsx",
    ),
    InfoNeeded(
        "Soil module- soil bulk density protocol",
        "https://linked.data.gov.au/def/test/dawe-cv/265eff6c-8ea2-4f9a-bcd1-09c5ff02e891",
        "https://linked.data.gov.au/def/test/dawe-cv/72b5340f-6654-4ee8-81dc-6a492964b20c",
        "https://linked.data.gov.au/def/test/dawe-cv/d9e6739a-c2dd-4619-be43-1251449a6436",
        "vocab-sources/second-stage/soil-soil-bulk-density-attributes.xlsx",
        "vocab-sources/second-stage/soil-soil-bulk-density-properties.xlsx",
    ),
    InfoNeeded(
        "Soil module- soil condition protocol",
        "https://linked.data.gov.au/def/test/dawe-cv/f6fa4714-5104-400a-a73d-dff7349248d8",
        "",
        "https://linked.data.gov.au/def/test/dawe-cv/1c83a60d-12e5-4bb3-b876-7eb97da79fa9",
        "vocab-sources/second-stage/soil-condition-attributes.xlsx",
        "",
    ),
    InfoNeeded(
        "Soil module- soil metagenomics protocol",
        "https://linked.data.gov.au/def/test/dawe-cv/52826869-2c3b-47ad-8060-776694e4a601",
        "",
        "https://linked.data.gov.au/def/test/dawe-cv/ca8a3a10-d35d-45ff-b987-a4ab3f1ce1c5",
        "vocab-sources/second-stage/soil-metagenomics-attributes.xlsx",
        "",
    ),
    InfoNeeded(
        "Invertebrate module- wet pitfall",
        "https://linked.data.gov.au/def/test/dawe-cv/e8c64fea-079b-47c3-be2d-d3844891a90d",
        "https://linked.data.gov.au/def/test/dawe-cv/0fff4578-8fb7-4da1-a197-5078cafb1b25",
        "https://linked.data.gov.au/def/test/dawe-cv/7e4bfab2-4056-4309-bd22-f070f6952bc0",
        "vocab-sources/second-stage/invertebrate-micropitfall-attributes.xlsx",
        "vocab-sources/second-stage/invertebrate-micropitfall-properties.xlsx",
    ),
    # InfoNeeded(
    #     "Invertebrate module- eDNA",
    #     "https://linked.data.gov.au/def/test/dawe-cv/f9f86714-4277-4c89-a6ce-f6c12ef1668d",
    #     "https://linked.data.gov.au/def/test/dawe-cv/860751a6-7fe8-418a-8a30-f88e060e49cd",
    #     "https://linked.data.gov.au/def/test/dawe-cv/0ad98270-707f-4a78-acd1-666faa2c124e",
    #     "vocab-sources/second-stage/invertebrate-edna-attributes.xlsx",
    #     "vocab-sources/second-stage/invertebrate-edna-properties.xlsx",
    # ),
    InfoNeeded(
        "Invertebrate module - Malaise trapping",
        "https://linked.data.gov.au/def/test/dawe-cv/dac32537-fa2a-4a58-a1f8-70715e7e4eb4",
        "https://linked.data.gov.au/def/test/dawe-cv/553e5dc9-db36-484c-b71c-75a9b76dcca5",
        "https://linked.data.gov.au/def/test/dawe-cv/4a2c4309-da43-4ad4-b1eb-637d2e70580d",
        "vocab-sources/second-stage/invertebrate-malaise-trapping-attributes.xlsx",
        "vocab-sources/second-stage/invertebrate-malaise-trapping-properties.xlsx",
    ),
    InfoNeeded(
        "Invertebrate module - leaf-litter extraction",
        "https://linked.data.gov.au/def/test/dawe-cv/a77c5dba-4941-45b7-bc15-fbd67ef8ebfd",
        "https://linked.data.gov.au/def/test/dawe-cv/b29538e9-1118-45c5-88d5-ba1738b57940",
        "https://linked.data.gov.au/def/test/dawe-cv/e9a8e65a-59d3-49f0-831d-094c568c5284",
        "vocab-sources/second-stage/invertebrate-leaf-litter-extraction-attributes.xlsx",
        "vocab-sources/second-stage/invertebrate-leaf-litter-extraction-properties.xlsx",
    ),
    InfoNeeded(
        "Invertebrate module - light trapping (LepiLED)",
        "https://linked.data.gov.au/def/test/dawe-cv/f4bb7c80-7faf-49c7-8ab9-7b0052e7aade",
        "https://linked.data.gov.au/def/test/dawe-cv/beacf237-e402-4911-a9e4-89925374df23",
        "https://linked.data.gov.au/def/test/dawe-cv/7d74d213-3fb8-46b4-9970-2544f555e279",
        "vocab-sources/second-stage/invertebrate-light-trapping-attributes.xlsx",
        "vocab-sources/second-stage/invertebrate-light-trapping-properties.xlsx",
    ),
    InfoNeeded(
        "Invertebrate module - pan trapping",
        "https://linked.data.gov.au/def/test/dawe-cv/ef22b1a2-87a9-4ac7-b98a-c4297e12de04",
        "https://linked.data.gov.au/def/test/dawe-cv/50054098-8127-4e09-b397-9e3c6d074570",
        "https://linked.data.gov.au/def/test/dawe-cv/666e5aa5-e545-4637-bc52-a296d647b303",
        "vocab-sources/second-stage/invertebrate-pan-trapping-attributes.xlsx",
        "vocab-sources/second-stage/invertebrate-pan-trapping-properties.xlsx",
    ),
    InfoNeeded(
        "Invertebrate module- active sampling",
        "https://linked.data.gov.au/def/test/dawe-cv/8128a20c-e8c7-45ba-9d8d-4d3347a6c34f",
        "https://linked.data.gov.au/def/test/dawe-cv/2d955edb-ab22-4101-bc72-b5899d901fd7",
        "https://linked.data.gov.au/def/test/dawe-cv/e76e99ef-de1d-4387-9b2e-3455b9f9ff78",
        "vocab-sources/second-stage/invertebrate-active-sampling-attributes.xlsx",
        "vocab-sources/second-stage/invertebrate-active-sampling-properties.xlsx",
    ),
    # InfoNeeded(
    #     "Invertebrate module- foliage beating",
    #     "https://linked.data.gov.au/def/test/dawe-cv/163c4191-9eaa-45fe-af10-b16d5e66bfeb",
    #     "https://linked.data.gov.au/def/test/dawe-cv/a43aa2ff-09df-4a2f-96e6-5b9e409a5ad3",
    #     "https://linked.data.gov.au/def/test/dawe-cv/0ad98270-707f-4a78-acd1-666faa2c124e",
    #     "vocab-sources/second-stage/invertebrate-foliage-beating-attributes.xlsx",
    #     "vocab-sources/second-stage/invertebrate-foliage-beating-properties.xlsx",
    # ),
    # InfoNeeded(
    #     "Invertebrate module - sweep netting",
    #     "https://linked.data.gov.au/def/test/dawe-cv/c1640181-9f1f-41ad-8e26-00b28fa7f1bf",
    #     "https://linked.data.gov.au/def/test/dawe-cv/14ebdb0d-66f1-4322-b81e-ec7187f79a1f",
    #     "https://linked.data.gov.au/def/test/dawe-cv/0ad98270-707f-4a78-acd1-666faa2c124e",
    #     "vocab-sources/second-stage/invertebrate-sweep-netting-attributes.xlsx",
    #     "vocab-sources/second-stage/invertebrate-sweep-netting-properties.xlsx",
    # ),
    InfoNeeded(
        "Invertebrate module - post-field guideline",
        "https://linked.data.gov.au/def/test/dawe-cv/9d643bf1-67b0-4f7d-9e74-c2dba44678dd",
        "https://linked.data.gov.au/def/test/dawe-cv/656138c9-abc3-44c5-8d69-3522de407dee",
        "https://linked.data.gov.au/def/test/dawe-cv/79296cab-a02f-420d-b260-17c0e8691499",
        "vocab-sources/second-stage/invertebrate-post-field-guideline-attributes.xlsx",
        "vocab-sources/second-stage/invertebrate-post-field-guideline-properties.xlsx",
    ),
    InfoNeeded(
        "Targeted survey - general field survey",
        "https://linked.data.gov.au/def/test/dawe-cv/5711a30b-d89f-4984-b488-af9943658f7a",
        "https://linked.data.gov.au/def/test/dawe-cv/ccaedec9-ffdc-42df-9c9f-7dce8b14fb91",
        "https://linked.data.gov.au/def/test/dawe-cv/420ce0a7-9364-4bf4-861c-ef5f710e31b9",
        "vocab-sources/second-stage/targeted-survey-general-field-attributes.xlsx",
        "vocab-sources/second-stage/targeted-survey-general-field-properties.xlsx",
    ),
    InfoNeeded(
        "Targeted survey - fauna protocol",
        "https://linked.data.gov.au/def/test/dawe-cv/2881bb3f-2c60-42f8-a812-b579f9f7c5e9",
        "",
        "https://linked.data.gov.au/def/test/dawe-cv/420ce0a7-9364-4bf4-861c-ef5f710e31b9",
        "vocab-sources/second-stage/targeted-survey-fauna-general-attributes.xlsx",
        "",
    ),
    InfoNeeded(
        "Targeted survey - fauna protocol- active",
        "https://linked.data.gov.au/def/test/dawe-cv/ce60bba4-736f-4ce3-b0ae-61d083d67a05",
        "https://linked.data.gov.au/def/test/dawe-cv/5a31ad93-8729-435d-b3ba-e361ab70a10c",
        "https://linked.data.gov.au/def/test/dawe-cv/420ce0a7-9364-4bf4-861c-ef5f710e31b9",
        "vocab-sources/second-stage/targeted-survey-fauna-active-attributes.xlsx",
        "vocab-sources/second-stage/targeted-survey-fauna-active-properties.xlsx",
    ),
    InfoNeeded(
        "Targeted survey - fauna protocol - passive",
        "https://linked.data.gov.au/def/test/dawe-cv/3789322d-6295-4efd-9c94-de60322c0ae1",
        "https://linked.data.gov.au/def/test/dawe-cv/5ed1bd2f-f3f3-4b62-a485-c07ccb454e66",
        "https://linked.data.gov.au/def/test/dawe-cv/420ce0a7-9364-4bf4-861c-ef5f710e31b9",
        "vocab-sources/second-stage/targeted-survey-fauna-passive-attributes.xlsx",
        "vocab-sources/second-stage/targeted-survey-fauna-passive-properties.xlsx",
    ),
    InfoNeeded(
        "Targeted survey - flora protocol",
        "https://linked.data.gov.au/def/test/dawe-cv/2a8b14a7-6685-4103-8078-2f82acb74be8",
        "",
        "https://linked.data.gov.au/def/test/dawe-cv/420ce0a7-9364-4bf4-861c-ef5f710e31b9",
        "vocab-sources/second-stage/targeted-survey-flora-general-attributes.xlsx",
        "",
    ),
    InfoNeeded(
        "Targeted survey - flora protocol- observation",
        "https://linked.data.gov.au/def/test/dawe-cv/f80e7296-e386-4bb5-b8c3-3cf8823050f5",
        "https://linked.data.gov.au/def/test/dawe-cv/9b5e04d5-182c-4644-8bba-4c8f6399b527",
        "https://linked.data.gov.au/def/test/dawe-cv/420ce0a7-9364-4bf4-861c-ef5f710e31b9",
        "vocab-sources/second-stage/targeted-survey-flora-observation-attributes.xlsx",
        "vocab-sources/second-stage/targeted-survey-flora-observation-properties.xlsx",
    ),
    InfoNeeded(
        "Targeted survey - flora protocol- population",
        "https://linked.data.gov.au/def/test/dawe-cv/5f8d2d74-ba78-4030-a346-78b671fedf6d",
        "https://linked.data.gov.au/def/test/dawe-cv/7a3a06af-8c03-414f-9040-fd4bbf691384",
        "https://linked.data.gov.au/def/test/dawe-cv/420ce0a7-9364-4bf4-861c-ef5f710e31b9",
        "vocab-sources/second-stage/targeted-survey-flora-population-attributes.xlsx",
        "vocab-sources/second-stage/targeted-survey-flora-population-properties.xlsx",
    ),
    InfoNeeded(
        "Targeted survey - Ecological community protocol",
        "https://linked.data.gov.au/def/test/dawe-cv/228ecdc5-9982-4049-9c15-db781d7e6e0f",
        "https://linked.data.gov.au/def/test/dawe-cv/2e7e218c-c307-4dfa-9560-90d8f03e401e",
        "https://linked.data.gov.au/def/test/dawe-cv/420ce0a7-9364-4bf4-861c-ef5f710e31b9",
        "vocab-sources/second-stage/targeted-survey-ecological-community-attributes.xlsx",
        "vocab-sources/second-stage/targeted-survey-ecological-community-properties.xlsx",
    ),
]

# Output file name.
output_filename = "output.ttl"
