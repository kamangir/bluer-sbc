from bluer_objects import README
from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url

from bluer_sbc.README.design import design_doc

assets2 = assets_url(
    suffix="anchor",
    volume=2,
)

marquee = README.Items(
    [
        {
            "name": "anchor",
            "marquee": f"{assets2}/03.png",
            "url": "./bluer_sbc/docs/anchor.md",
        }
    ]
)

items = ImageItems(
    {
        f"{assets2}/03.jpg": "",
    }
)

parts = {
    # TBA
}


docs = [
    design_doc(
        "anchor",
        items,
        parts,
    )
]
