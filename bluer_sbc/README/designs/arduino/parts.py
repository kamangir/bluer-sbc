from bluer_sbc.README.design import design_doc_parts

parts = {
    "470-mF": "",
    "arduino-nano": "",
    "dc-switch": "small",
    "HC-05": "",
    "hw-373-charger": "",
    "LED": "2 x blue",
    "li-ion-battery": "18650, 3.6v, 3350mAh, with holder",
    "mt-3608": "",
    "nuts-bolts-spacers": "M3: ({})".format(
        " + ".join(
            [
                "4 x bolt",
                "4 x nut",
                "8 x 25 mm spacer",
            ]
        )
    ),
    "PCB-double-9x7": "",
    "pin-headers": "2 x (male header, 1 x 40)",
    "plexiglass": "2 x 9 cm x 7 cm",
    "pushbutton": "1",
    "resistor": "2 x 330 Ω + 1 x 1 kΩ",
}

docs = [
    {
        "path": "../docs/arduino/parts.md",
        "macros": design_doc_parts(
            dict_of_parts=parts,
            parts_reference="repo",
        ),
    }
]
