from bluer_sbc.README.design import design_doc_parts

parts = {
    "arduino-nano": "",
    "dc-switch": "small",
    "dfplayer-mini": "max 3 W output into 4 Ω at 5 V ~= class-D amp",
    "li-ion-battery": "18650, 3.6v, 3350mAh",
    "mt-3608": "",
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
