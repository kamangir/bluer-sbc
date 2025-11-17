from bluer_objects import README

from bluer_sbc.README.designs.consts import assets2

latest_version: int = 5

image_template = assets2 + f"swallow/design/v{latest_version}/{{}}?raw=true"

marquee = README.Items(
    [
        {
            "name": "swallow",
            "marquee": image_template.format("01.jpg"),
            "url": "./bluer_sbc/docs/swallow",
        }
    ]
)
