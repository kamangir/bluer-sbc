from bluer_objects import README
from bluer_objects.README.consts import assets_url

image_template = assets_url(
    suffix="arduino/{}?raw=true",
    volume=3,
)

marquee = README.Items(
    [
        {
            "name": "arduino dev box",
            "marquee": image_template.format("IMG_0151.JPG"),
            "url": "./bluer_sbc/docs/arduino",
        }
    ]
)
