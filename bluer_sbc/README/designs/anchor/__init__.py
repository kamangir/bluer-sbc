from bluer_objects import README
from bluer_objects.README.consts import assets_url

image_template = assets_url(
    suffix="anchor/{}?raw=true",
    volume=2,
)

marquee = README.Items(
    [
        {
            "name": "anchor ⚓️",
            "marquee": image_template.format("20251205_175953.jpg"),
            "url": "./bluer_sbc/docs/anchor",
        }
    ]
)
