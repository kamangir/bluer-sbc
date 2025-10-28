from bluer_objects import README
from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.consts import assets2

image_template = assets2 + "nafha/{}?raw=true"

marquee = README.Items(
    [
        {
            "name": "nafha",
            "marquee": image_template.format("01.png"),
            "url": "./bluer_sbc/docs/nafha",
        }
    ]
)

items = ImageItems(
    {
        **{image_template.format(f"{index+1:02}.png"): "" for index in range(4)},
        **{
            assets2.format(f"{filename}.jpg"): ""
            for filename in [
                "20251028_123428",
                "20251028_123438",
            ]
        },
    }
)
