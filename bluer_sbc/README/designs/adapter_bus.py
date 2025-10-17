from bluer_objects import README
from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url

assets2 = assets_url(
    suffix="adapter-bus",
    volume=2,
)

marquee = README.Items(
    [
        {
            "name": "adapter bus",
            "marquee": f"{assets2}/TBA.jpg",
            "url": "./bluer_sbc/docs/adapter-bus.md",
        }
    ]
)

items = ImageItems(
    {
        # f"{assets2}/TBA.jpg": "",
    }
)
