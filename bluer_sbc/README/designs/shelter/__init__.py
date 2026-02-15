from bluer_objects import README
from bluer_objects.README.consts import assets_url

image_template = assets_url(
    suffix="shelter/{}",
    volume=2,
)


marquee = README.Items(
    [
        {
            "name": "shelter",
            "marquee": image_template.format("20251104_000755.jpg"),
            "url": "./bluer_sbc/docs/shelter",
        }
    ]
)
