from bluer_objects import README
from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_path

from bluer_sbc.README.designs.consts import assets2

image_template = assets2 + "battery_bus/{}?raw=true"

assets2_battery_bus = assets_path(
    suffix="battery_bus",
    volume=2,
)

marquee = README.Items(
    [
        {
            "name": "battery_bus",
            "marquee": f"{assets2_battery_bus}/concept.png",
            "url": "./bluer_sbc/docs/battery-bus.md",
        }
    ]
)

items = ImageItems(
    {
        f"{assets2_battery_bus}/concept.png": "",
    }
)
