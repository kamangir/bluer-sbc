from bluer_sbc.README.design import design_doc_parts

parts = {
    "220VAC-dimmer": "",
    "resistance-heating-wire": "1.59 kΩ",
    "mountable-digital-thermometer": "",
    "ac-volt-meter": "220 V, 1 A",
}

docs = [
    {
        "path": "../docs/shelter/couch/parts/",
        "macros": design_doc_parts(
            dict_of_parts=parts,
            parts_reference="../parts",
        ),
    }
] + [
    {
        "path": "../docs/shelter/couch/parts/v1.md",
    },
]
