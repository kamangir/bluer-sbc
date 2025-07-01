import os
from typing import List

from bluer_objects import file, README

from bluer_sbc import NAME, VERSION, ICON, REPO_NAME


items = README.Items(
    [
        {
            "name": item["name"],
            "marquee": "https://github.com/kamangir/assets2/blob/main/bluer-swallow/design/{}?raw=true".format(
                item["image"]
            ),
            "url": "TBA/{}".format(item["name"]),
        }
        for item in [
            {
                "image": "06.jpg",
                "name": "bluer-swallow",
            },
            {
                "image": "08.jpg",
                "name": "bryce",
            },
        ]
    ]
) + README.Items(
    [
        {
            "name": item["name"],
            "marquee": "https://github.com/kamangir/blue-bracket/raw/main/images/{}".format(
                item["image"]
            ),
            "url": "https://github.com/kamangir/blue-bracket/blob/main/designs/{}".format(
                item["name"]
            ),
        }
        for item in [
            {
                "image": "blue3-1.jpg",
                "name": "blue3",
            },
            {
                "image": "chenar-grove-1.jpg",
                "name": "chenar-grove",
            },
            {
                "image": "cube-1.jpg",
                "name": "cube",
            },
            {
                "image": "eye_nano-1.jpg",
                "name": "eye_nano",
            },
        ]
    ]
)

x = [
    "[![image]({}{})]({}{}.md)".format(
        "https://github.com/kamangir/assets/TBA",
        item["image"],
        "https://github.com/kamangir/bluer-sbc/bluer_sbc/docs/",
        item["name"],
    )
    for item in []
]

bluer_swallow_items = []

bryce_items = []


def build():
    return all(
        README.build(
            items=readme.get("items", []),
            cols=readme.get("cols", 3),
            path=os.path.join(file.path(__file__), readme["path"]),
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
        )
        for readme in [
            {"items": items, "path": ".."},
            {"items": bluer_swallow_items, "path": "./docs/bluer-swallow.md"},
            {"items": bryce_items, "path": "./docs/bryce.md"},
        ]
    )
