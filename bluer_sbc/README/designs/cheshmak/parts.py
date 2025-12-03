from bluer_sbc.README.design import design_doc

parts = {
    "plexiglass": "2 x 90 mm x 90 mm",
    "rpi": "",
    "rpi-camera": "",
    "nuts-bolts-spacers": "M2.5: ({})".format(
        " + ".join(
            [
                "4 x bolt",
                "4 x nut",
                "12 x 10 mm spacer",
                "4 x 15 mm spacer",
            ]
        )
    ),
}


docs = [
    {
        "path": "../docs/cheshmak/parts.md",
        "macros": {
            keyword: value
            for keyword, value in design_doc(
                "cheshmak",
                dict_of_parts=parts,
            )["macros"].items()
            if keyword.startswith("parts_")
        },
    }
]
