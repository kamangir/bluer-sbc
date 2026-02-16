from bluer_objects import README
from bluer_objects.README.consts import assets_url

image_template = assets_url(
    suffix="battery-bus/{}?raw=true",
    volume=2,
)

marquee = README.Items(
    [
        {
            "name": "battery bus",
            "marquee": image_template.format("20251007_221902.jpg"),
            "url": "./bluer_sbc/docs/battery_bus",
        }
    ]
)
