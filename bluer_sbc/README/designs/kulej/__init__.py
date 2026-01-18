from bluer_objects import README

from bluer_sbc.README.designs.consts import assets2

image_template = assets2 + "kulej/{}?raw=true"

marquee = README.Items(
    [
        {
            "name": "kulej ⛰️",
            "marquee": image_template.format("20260118_142743.jpg"),
            "url": "./bluer_sbc/docs/kulej",
        }
    ]
)
