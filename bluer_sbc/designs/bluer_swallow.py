from bluer_objects import README

design_template = "TBA/{}.md"

image_template = (
    "https://github.com/kamangir/assets2/blob/main/bluer-swallow/design/{}?raw=true"
)

marquee = README.Items(
    [
        {
            "name": item["name"],
            "marquee": image_template.format(item["image"]),
            "url": design_template.format(item["name"]),
        }
        for item in [
            {
                "image": "06.jpg",
                "name": "bluer-swallow",
            },
        ]
    ]
)

items = []
