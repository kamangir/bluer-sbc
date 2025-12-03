from bluer_objects import README
from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.consts import assets2
from bluer_sbc.README.design import design_doc

image_template = assets2 + "cheshmak/{}?raw=true"

marquee = README.Items(
    [
        {
            "name": "cheshmak",
            "marquee": image_template.format("20251203_190131.jpg"),
            "url": "./bluer_sbc/docs/cheshmak",
        }
    ]
)

items = ImageItems(
    {
        (assets2 + "bryce/{}?raw=true").format(f"{9:02}.jpg"): "",
        **{image_template.format(f"{index+1:02}.png"): "" for index in range(1)},
        **{
            image_template.format(filename): ""
            for filename in [
                "20251203_190131.jpg",
                "20251203_190344.jpg",
            ]
        },
    }
)


docs = [
    design_doc(
        "cheshmak",
        items,
        own_folder=True,
    ),
    {
        "path": "../docs/cheshmak/v1.md",
        "items": ImageItems(
            {
                **{
                    (assets2 + "bryce/{}?raw=true").format(f"{index+1:02}.jpg"): ""
                    for index in range(8)
                }
            }
        ),
    },
    {
        "path": "../docs/cheshmak/operation.md",
    },
]
