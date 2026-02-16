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
            "marquee": assets_url(
                suffix="bluer-sbc/parts/arduino-nano.png?raw=true",
                volume=2,
            ),
            "url": "./bluer_sbc/docs/arduino",
        }
    ]
)
