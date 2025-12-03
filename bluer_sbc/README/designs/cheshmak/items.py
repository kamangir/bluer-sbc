from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.cheshmak import assets2, image_template

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
