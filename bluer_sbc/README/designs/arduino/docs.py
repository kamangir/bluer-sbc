from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.arduino import image_template, parts, schematics

docs = (
    [
        {
            "path": "../docs/arduino",
            "items": ImageItems(
                {
                    image_template.format("IMG_0151.JPG"): "",
                }
            ),
        }
    ]
    + parts.docs
    + schematics.docs
)
