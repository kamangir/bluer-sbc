from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.anchor import image_template

docs = [
    {
        "path": "../docs/anchor/body",
        "items": ImageItems(
            {
                image_template.format("TBA.jpg"): "",
            }
        ),
    }
]
