from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.cheshmak import image_template
from bluer_sbc.README.designs.cheshmak.body import v1, v2

docs = (
    [
        {
            "path": "../docs/cheshmak/body",
            "items": ImageItems(
                {
                    # image_template.format("TBA.jpg"): "",
                }
            ),
        }
    ]
    + v1.docs
    + v2.docs
)
