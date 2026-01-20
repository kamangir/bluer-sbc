from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.isatis import image_template

docs = [
    {
        "path": "../docs/isatis/body",
        "items": ImageItems(
            {
                image_template.format("01.png"): "",
            }
        ),
    }
]
