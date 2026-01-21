from bluer_sbc.README.design import design_doc_parts

parts = {
    "470-mF": "",
    "arduino-nano": "",
    "dc-power-plug": "",
    "dc-switch": "small",
    "dfplayer-mini": "max 3 W output into 4 Ω at 5 V ~= class-D amp",
    "LED": "1 x blue",
    "li-ion-battery": "18650, 3.6v, 3350mAh",
    "li-ion-charger": "",
    "mt-3608": "",
    "pushbutton": "",
    "resistor": "1 x 220-330 Ω + 1 x 1 kΩ",
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
