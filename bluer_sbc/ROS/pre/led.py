import RPi.GPIO as GPIO  # type: ignore

from bluer_sbc.logger import logger


class PreROSLeds:
    def __init__(self):
        self.leds = {
            "yellow": {"pin": 17, "state": True},
            "red": {"pin": 27, "state": False},
            "green": {"pin": 22, "state": True},
        }

    def initialize(self) -> bool:
        try:
            for led in self.leds.values():
                GPIO.setup(
                    led["pin"],
                    GPIO.OUT,
                )
        except Exception as e:
            logger.error(e)
            return False

        return True
