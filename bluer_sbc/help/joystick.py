from typing import List

from bluer_options.terminal import show_usage, xtra


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@joystick",
            "install",
        ],
        "install joystick.",
        mono=mono,
    )


def help_validate(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "install",
            xtra(",~use_python", mono=mono),
        ]
    )

    return show_usage(
        [
            "@joystick",
            "validate",
            f"[{options}]",
        ],
        "validate joystick.",
        mono=mono,
    )


help_functions = {
    "install": help_install,
    "validate": help_validate,
}
