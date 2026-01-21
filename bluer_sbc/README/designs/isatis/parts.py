from bluer_sbc.README.design import design_doc_parts

parts = {
    "arduino-nano": "",
    "dc-switch": "small",
    "dfplayer-mini": "max 3 W output into 4 Ω at 5 V ~= class-D amp",
    "li-ion-battery": "26650, 5000 mAh 5C, 3.7 V/4.2 V 🔥",
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
