from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.arduino import image_template, body, parts, schematics

docs = (
    [
        {
            "path": "../docs/arduino",
            "items": ImageItems(
                {
                    image_template.format("IMG_0151.JPG"): "",
                    image_template.format("serial-plotter.gif"): "",
                }
            ),
            "cols": 1,
        }
    ]
    + body.docs
    + parts.docs
    + schematics.docs
)
