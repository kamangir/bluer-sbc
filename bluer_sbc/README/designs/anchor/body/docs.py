from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.anchor import image_template
from bluer_sbc.README.designs.anchor.body import v1

docs = [
    {
        "path": "../docs/anchor/body",
        "items": ImageItems(
            {
                image_template.format("20251205_171731.jpg"): "",
                image_template.format("20251205_175910.jpg"): "",
                image_template.format("20251205_175916.jpg"): "",
                image_template.format("20251205_175920.jpg"): "",
                image_template.format("20251205_175932.jpg"): "",
                image_template.format("20251205_175936.jpg"): "",
                image_template.format("20251205_175941.jpg"): "",
                image_template.format("20251205_175953.jpg"): "",
            }
        ),
    }
] + v1.docs
