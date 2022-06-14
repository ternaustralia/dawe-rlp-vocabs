from dawe_vocabs.schemas import LUTSchema, ExcelVocab


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
        "https://dev.core-api.paratoo.tern.org.au/lut-fauna-genders",
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
        "vocab-sources/first-stage/photopoints-attributes-collection.xlsx",
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
    ExcelVocab(
        "vocab-sources/second-stage/basal-area-attributes.xlsx",
        "1XlrN9Lf2s5DPxOBLu4oMmvk8efBOtSGl",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/basal-area-properties-collection.xlsx",
        "12u4WnYitHLDuYDECSmqyxhRexYUvcFqR",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/basal-area-properties.xlsx",
        "1nuRUsQzXz6K7lmzAMTTJ_cmYVh1LRLt0",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/coarse-woody-debris-attributes-collection.xlsx",
        "17qCVHfj7Aio3BKhiLiIKZQAava2ceWSx",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/coarse-woody-debris-attributes.xlsx",
        "1e-FZklwVaSt8n-WA24vq54aOl-gznFMH",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/coarse-woody-debris-properties-collection.xlsx",
        "1E6oBGu-lcqpjCir99kDeZ5HyKxvKUBvg",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/coarse-woody-debris-properties.xlsx",
        "1FYsYuozWG9IFYUR6xNqpnV1vL6tW2oXh",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/condition-attributes-collection.xlsx",
        "1Izsg_5cBqJVyeLIwiY32ZzUTi1AHlgTc",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/condition-attributes.xlsx",
        "1BEi6UAYVqL1WR5rtBW4oBXlvYuCGaMEm",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/condition-properties-collection.xlsx",
        "1YP4Gm58oQ3Vdg_Uupszyif4NOQXoSIF4",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/condition-properties.xlsx",
        "1_n1W68h7-wzsqFx6mLws46rG3y5sXD7V",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/fire-attributes-collection.xlsx",
        "1KMQNMZKWvYALgXkZqipRE0M-gZtG4KrR",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/fire-attributes.xlsx",
        "1Vf0H8D8_G27G25SfgZJFGjG08p-NhPxD",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/fire-properties-collection.xlsx",
        "1DPHQmvCZl2pp1Ve4DyQIRVJQGGmQvajU",
    ),
    ExcelVocab(
        "vocab-sources/second-stage/fire-properties.xlsx",
        "1i_eHyoP6P1IQdqAMe9UPyrxyMD-1aqdh",
    ),
)

# Output file name.
output_filename = "output.ttl"
