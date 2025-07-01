from bluer_objects import README


image_template = (
    "https://github.com/kamangir/assets2/blob/main/bluer-swallow/design/{}?raw=true"
)

marquee = README.Items(
    [
        {
            "name": "bluer-swallow",
            "marquee": image_template.format("06.jpg"),
            "url": "./bluer_sbc/docs/bluer-swallow.md",
        }
    ]
)

items = []
