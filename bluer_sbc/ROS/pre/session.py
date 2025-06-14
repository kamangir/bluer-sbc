import RPi.GPIO as GPIO  # type: ignore

from bluer_sbc.ROS.pre.button import PreROSButton
from bluer_sbc.ROS.pre.led import PreROSLeds
from bluer_sbc.logger import logger


class PreROSSession:
    def __init__(self):
        self.button = PreROSButton()
        self.leds = PreROSLeds()

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
