from bluer_objects import README
from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url, designs_url

from bluer_sbc.README.design import design_doc


assets2 = assets_url(
    suffix="pwm-generator",
    volume=2,
)

marquee = README.Items(
    [
        {
            "name": "regulated bus",
            "marquee": f"{assets2}/TBA.jpg",
            "url": "./bluer_sbc/docs/pwm-generator.md",
        }
    ]
)

items = ImageItems(
    {
        designs_url(
            "pwm-generator/wiring.png?raw=true",
        ): designs_url(
            "pwm-generator/wiring.svg",
        ),
        **{
            f"{assets2}/{timestamp}.jpg": ""
            for timestamp in [
                "TBA",
            ]
        },
    }
)

parts = {
    "dc-power-plug": "",
    "dc-power-jack": "",
    "dsn-vc288": "",
    "plexiglass": "2 x 80 cm x 100 cm",
    "pwm-manual-dc-motor-controller": "",
    "nuts-bolts-spacers": "M3: ({})".format(
        " + ".join(
            [
                "4 x bolt",
                "4 x nut",
                "4 x 40 mm spacer",
            ]
        )
    ),
}


docs = [
    design_doc(
        "pwm-generator",
        items,
        parts,
    )
]
