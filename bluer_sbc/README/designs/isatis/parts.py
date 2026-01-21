from bluer_sbc.README.design import design_doc_parts

parts = {
    "arduino-nano": "",
    "dfplayer-mini": "max 3 W output into 4 Ω at 5 V ~= class-D amp",
    "speaker": "passive, ≥ 3 W, 4 Ω (loudest) or 8 Ω (safer, quieter)",
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
