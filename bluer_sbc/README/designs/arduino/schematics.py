from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import designs_url

docs = [
    {
        "path": "../docs/arduino/schematics.md",
        "items": ImageItems(
            {
                designs_url(
                    "arduino/schematics.png",
                ): designs_url(
                    "arduino/schematics.svg",
                ),
            }
        ),
    }
]
