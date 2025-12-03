from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.cheshmak import assets2, image_template

items = ImageItems(
    {
        **{image_template.format(f"{index+1:02}.png"): "" for index in range(1)},
        (assets2 + "bryce/{}?raw=true").format(f"{9:02}.jpg"): "",
    }
)
