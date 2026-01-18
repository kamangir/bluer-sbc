from bluer_sbc.README.design import design_doc_parts

parts = {
    "16-awg-wire": "20 cm x (red + black/blue)",
    "dc-power-plug": "",
    "dc-switch": "",
    "dsn-vc288": "",
    "li-ion-battery": "3 x 26650, 5000 mAh 5C, 3.7 V/4.2V",
    "nuts-bolts-spacers": " + ".join(
        [
            "M2.5: ({})".format(
                " + ".join(
                    [
                        "4 x bolt",
                        "4 x nut",
                        "8 x 10 mm spacer",
                    ]
                )
            ),
            "M3: ({})".format(
                " + ".join(
                    [
                        "5 x bolt",
                        "5 x nut",
                        "5 x 15 mm spacer",
                        "4 x 25 mm spacer",
                        "4 x 35 mm spacer",
                    ]
                )
            ),
        ]
    ),
    "PCB-single-14x9_5": "",
    "plexiglass": "2 x 14 cm x 9.5 cm",
    "rpi": "",
    "sd-card-32-gb": "",
    "solid-cable-1-15": "10 cm x (red + black/blue)",
    "swallow-shield": "",
    "XL4015": "",
}

docs = [
    {
        "path": "../docs/kulej/parts.md",
        "macros": design_doc_parts(
            dict_of_parts=parts,
            parts_reference="../parts",  # TBF
        ),
    }
]
