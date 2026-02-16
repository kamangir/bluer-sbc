from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url

docs = [
    {
        "path": "../docs/cheshmak/validations.md",
        "items": ImageItems(
            {
                assets_url(
                    suffix="bryce/09.jpg?raw=true",
                    volume=2,
                ): "",
            }
        ),
    },
]
