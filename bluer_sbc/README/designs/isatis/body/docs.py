from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.kulej import image_template

docs = [
    {
        "path": "../docs/isatis/body",
        "items": ImageItems(
            {
                image_template.format("TBA.jpg"): "",
            }
        ),
    }
]
