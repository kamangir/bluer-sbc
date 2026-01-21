from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import designs_url


docs = [
    {
        "path": "../docs/isatis/schematics.md",
        "items": ImageItems(
            {
                designs_url(
                    "isatis/schematics.png?raw=true",
                ): designs_url(
                    "isatis/schematics.svg",
                ),
            }
        ),
    },
]
