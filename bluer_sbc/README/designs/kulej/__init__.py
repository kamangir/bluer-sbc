from bluer_objects import README

from bluer_sbc.README.designs.consts import assets2

image_template = assets2 + "kulej/{}?raw=true"

marquee = README.Items(
    [
        {
            "name": "kulej ⛰️",
            "marquee": "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true",  # image_template.format("TBA"),
            "url": "./bluer_sbc/docs/kulej",
        }
    ]
)
