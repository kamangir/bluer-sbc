from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url

image_template = assets_url(
    suffix="bryce/{}?raw=true",
    volume=2,
)

docs = [
    {
        "path": "../docs/cheshmak/body/v1.md",
        "items": ImageItems(
            {
                **{
                    image_template.format(
                        f"{index+1:02}.jpg",
                    ): ""
                    for index in range(8)
                }
            }
        ),
    },
]
