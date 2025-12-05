from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import designs_url

from bluer_sbc.README.designs.battery_bus import image_template

items = ImageItems(
    {
        image_template.format("concept.png"): "",
        designs_url(
            "battery-bus/electrical/wiring.png?raw=true",
        ): designs_url(
            "battery-bus/electrical/wiring.svg",
        ),
        image_template.format("20251007_221902.jpg"): "",
        image_template.format("20251007_220642.jpg"): "",
        image_template.format("20251007_220520.jpg"): "",
        image_template.format("20251007_220601.jpg"): "",
    }
)
