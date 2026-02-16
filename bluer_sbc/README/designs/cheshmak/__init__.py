from bluer_objects import README
from bluer_objects.README.consts import assets_url

image_template = assets_url(
    suffix="cheshmak/{}?raw=true",
    volume=2,
)

marquee = README.Items(
    [
        {
            "name": "cheshmak 👁️",
            "marquee": image_template.format("20251203_190131.jpg"),
            "url": "./bluer_sbc/docs/cheshmak",
        }
    ]
)
