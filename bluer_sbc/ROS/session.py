import keyboard
import time

from blueness import module

from bluer_sbc import NAME
from bluer_sbc.session.functions import reply_to_bash
from bluer_sbc.logger import logger

NAME = module.name(__file__, NAME)

bash_keys = {
    "e": "exit",
    "r": "reboot",
    "s": "shutdown",
    "u": "update",
}


def start_session() -> bool:
    logger.info(
        "{}.start_session: {}".format(
            NAME,
            ", ".join(
                [f"{key}:{action}" for key, action in bash_keys.items()],
            ),
        )
    )

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            logger.info(f"key pressed: {key}")

            if key in bash_keys:
                reply_to_bash(bash_keys[key])
                return True
