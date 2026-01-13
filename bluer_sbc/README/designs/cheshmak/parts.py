from bluer_sbc.README.design import design_doc_parts

parts = {
    "dc-power-plug": "",
    "dc-switch": "",
    "PCB-single-14x9_5": "",
    "plexiglass": "...",
    "rpi": "",
    "nuts-bolts-spacers": ", ".join(
        [
            "M2.5: ({})".format(
                " + ".join(
                    [
                        "4 x bolt",
                        "4 x nut",
                        "12 x 10 mm spacer",
                    ]
                )
            ),
            "M3: ({})".format(
                " + ".join(
                    [
                        "4 x bolt",
                        "5 x nut",
                        "4 x 15 mm spacer",
                        "5 x 25 mm spacer",
                    ]
                )
            ),
        ]
    ),
    "XL4015": "",
}


docs = [
    {
        "path": "../docs/cheshmak/parts.md",
        "macros": design_doc_parts(
            dict_of_parts=parts,
            parts_reference="../parts",
        ),
    }
]
