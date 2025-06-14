import keyboard
import RPi.GPIO as GPIO  # type: ignore

from bluer_sbc.session.functions import reply_to_bash

from bluer_sbc.ROS.pre.button import PreROSButton
from bluer_sbc.ROS.pre.led import PreROSLeds
from bluer_sbc.logger import logger

bash_keys = {
    "e": "exit",
    "r": "reboot",
    "s": "shutdown",
    "u": "update",
}


class PreROSSession:
    def __init__(self):
        self.button = PreROSButton()
        self.leds = PreROSLeds()

        logger.info("{} created: {}".format)(
            PreROSSession.__class__.__name__,
            ", ".join(
                [f"{key}:{action}" for key, action in bash_keys.items()],
            ),
        )

    def initialize(self) -> bool:
        try:
            GPIO.setmode(GPIO.BCM)
        except Exception as e:
            logger.error(e)
            return False

        if not self.button.initialize():
            return False

        if not self.leds.initialize():
            return False

        return True

    def is_key_pressed(self) -> bool:
        for key, event in bash_keys.items():
            if keyboard.is_pressed(key):
                reply_to_bash(event)
                return True

        return False
