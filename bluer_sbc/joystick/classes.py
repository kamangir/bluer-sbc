import pygame
from typing import Dict

from bluer_sbc.logger import logger


class Joystick:
    def __init__(self):
        pygame.init()

        self.dict_of_buttons: Dict[int, str]
        self.dict_of_axes: Dict[int, int]

        joystick_count = pygame.joystick.get_count()
        if joystick_count > 1:
            logger.warning("{} joysticks found.")

        self.enabled: bool = joystick_count == 1
        self.joystick = None
        if self.enabled:
            logger.info("🕹️ detected.")

            self.joystick = pygame.joystick.Joystick(0)

            self.joystick.init()

            # Set up a clock to control the loop speed
            self.clock = pygame.time.Clock()

    @staticmethod
    def cleanup():
        pygame.quit()
