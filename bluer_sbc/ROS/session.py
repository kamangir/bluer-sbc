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
    logger.info(f"{NAME}.start_session...")

    while True:
        for key, action in bash_keys.items():
            if keyboard.is_pressed(key):
                reply_to_bash(action)
                return False

        time.sleep(0.1)
