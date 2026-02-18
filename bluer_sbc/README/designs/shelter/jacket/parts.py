from bluer_sbc.README.design import design_doc_parts

parts = {
    "dsn-vc288": "",
    "li-ion-battery": "3 x 26650, 5000 mAh 5C, 3.7 V/4.2V",
    "mountable-digital-thermometer": "",
    "pwm-manual-dc-motor-controller": "",
    "resistance-heating-wire": "TBA",
}


docs = [
    {
        "path": "../docs/shelter/jacket/parts.md",
        "macros": design_doc_parts(
            dict_of_parts=parts,
            parts_reference="../parts",
        ),
    }
]
