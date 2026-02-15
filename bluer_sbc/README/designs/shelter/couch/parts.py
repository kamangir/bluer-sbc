from bluer_sbc.README.design import design_doc_parts

parts = {
    "220VAC-dimmer": "",
    "ac-volt-meter": "220 V, 1 A",
    "mountable-digital-thermometer": "",
    "nuts-bolts-spacers": "M3: ({})".format(
        " + ".join(
            [
                "4 x bolt",
                "4 x nut",
                "4 x 35 mm spacer",
            ]
        )
    ),
    "plexiglass": "2 x 9 cm x 7 cm",
    "resistance-heating-wire": "1.59 kΩ",
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
