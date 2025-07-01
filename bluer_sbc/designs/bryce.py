from bluer_objects import README

image_template = "https://github.com/kamangir/assets2/blob/main/bryce/{}?raw=true"

marquee = README.Items(
    [
        {
            "name": "bryce",
            "marquee": image_template.format("08.jpg"),
            "url": "./bluer_sbc/docs/bryce.md",
        }
    ]
)

items = []
