from bluer_objects import README

from bluer_sbc.README.designs.consts import assets2

image_template = assets2 + "isatis/{}?raw=true"

marquee = README.Items(
    [
        {
            "name": "isatis 🔊",
            "marquee": image_template.format("TBA"),
            "url": "./bluer_sbc/docs/isatis",
        }
    ]
)
