from bluer_sbc.README.design import design_doc_parts

parts = {
    "arduino-nano": "",
    "dfplayer-mini": "max 3 W output",
}

docs = [
    {
        "path": "../docs/isatis/parts.md",
        "macros": design_doc_parts(
            dict_of_parts=parts,
            parts_reference="../parts",
        ),
    }
]
