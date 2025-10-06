from bluer_objects import README
from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_path

from bluer_sbc.designs.consts import assets2

image_template = assets2 + "shelter/{}?raw=true"

assets2_shelter = assets_path(
    suffix="shelter",
    volume=2,
)

marquee = README.Items(
    [
        {
            "name": "shelter",
            "marquee": image_template.format("01.png"),
            "url": "./bluer_sbc/docs/shelter.md",
        }
    ]
)

items = README.Items(
    [
        {
            "marquee": image_template.format(f"{index+1:02}.png"),
            "name": "",
        }
        for index in range(4)
    ]
    + ImageItems(
        {
            f"{assets2_shelter}/20251005_180841.jpg": "",
        }
    )
)
