import keyboard
import time
import RPi.GPIO as GPIO  # type: ignore

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

BUTTON_PIN = 26  # GPIO number (not physical pin)


def start_session() -> bool:
    logger.info(
        "{}.start_session: {}".format(
            NAME,
            ", ".join(
                [f"{key}:{action}" for key, action in bash_keys.items()],
            ),
        )
    )

    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    except Exception as e:
        logger.error(e)
        return False

    exit_flag: bool = False

    try:
        while not exit_flag:
            for key, event in bash_keys.items():
                if keyboard.is_pressed(key):
                    reply_to_bash(event)
                    exit_flag = True
                    break

            button_state = GPIO.input(BUTTON_PIN)
            if button_state:
                logger.info("button pressed.")

            time.sleep(0.1)
    except KeyboardInterrupt:
        logger.info("^C received.")
        return False
    finally:
        GPIO.cleanup()

    return True
