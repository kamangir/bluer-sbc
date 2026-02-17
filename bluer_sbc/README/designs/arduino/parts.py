from bluer_sbc.README.design import design_doc_parts

parts = {
    "470-mF": "",
    "arduino-nano": "",
    "dc-switch": "small",
    "dupont-cables": "10 cm",
    "HC-05": "",
    "hw-373-charger": "",
    "LED": "2 x blue + 1 x RGB",
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
    "potentiometer": "10 kΩ",
    "pushbutton": "1",
    "resistor": "5 x 330 Ω",
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
