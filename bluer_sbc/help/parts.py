from typing import List

from bluer_options.terminal import show_usage

from bluer_sbc import ALIAS


def help_adjust(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "dryrun"

    args = [
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@sbc",
            "parts",
            "adjust",
            f"[{options}]",
        ]
        + args,
        "adjust part images.",
        mono=mono,
    )


help_functions = {
    "adjust": help_adjust,
}
