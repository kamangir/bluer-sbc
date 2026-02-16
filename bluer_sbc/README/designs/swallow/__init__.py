from bluer_objects import README
from bluer_objects.README.consts import assets_url

latest_version: int = 6


def image_template(version: int) -> str:
    return assets_url(
        suffix=f"swallow/design/v{version}/{{}}?raw=true",
        volume=2,
    )


marquee = README.Items(
    [
        {
            "name": "swallow",
            "marquee": image_template(latest_version).format("01.jpg"),
            "url": "./bluer_sbc/docs/swallow",
        }
    ]
)
