from typing import Dict, List
import pygame
from pygame.event import Event

from bluer_sbc.logger import logger


class Joystick:
    def __init__(self):
        pygame.init()

        self.dict_of_buttons: Dict[int, str]
        self.dict_of_axes: Dict[int, int]

        self.axes: Dict[int, Event]
        self.buttons: Dict[int, Event]
        self.commands: List[Event]

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

    def read_events(self):
        self.axes = {}
        self.buttons = {}
        self.commands = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.commands.append(event)
                logger.info(
                    "{}: QUIT received.".format(
                        self.__class__.__name__,
                    )
                )

            if event.type == pygame.JOYBUTTONDOWN:
                logger.info(
                    "{}: button {} pressed.".format(
                        self.__class__.__name__,
                        event.button,
                    )
                )
                self.buttons[event.button] = event

            if event.type == pygame.JOYBUTTONUP:
                logger.info(
                    "{}: button {} released.".format(
                        self.__class__.__name__,
                        event.button,
                    )
                )
                self.buttons[event.button] = event

            if event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = event.value

                logger.info(
                    "{}: axis {} moved to {}.".format(
                        self.__class__.__name__,
                        axis,
                        value,
                    )
                )

                self.axes[event.axis] = event
