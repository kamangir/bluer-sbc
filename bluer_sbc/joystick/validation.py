import pygame
from pygame import JOYAXISMOTION, JOYBUTTONDOWN, JOYBUTTONUP, QUIT

from blueness import module

from bluer_sbc import NAME
from bluer_sbc.logger import logger


NAME = module.name(__file__, NAME)


def validate() -> bool:
    logger.info(f"{NAME}.validate...")

    pygame.init()

    joystick_count = pygame.joystick.get_count()
    if not joystick_count:
        logger.error("joystick not found.")
        return False
    if joystick_count > 1:
        logger.warning("{} joysticks found.")

    joystick = pygame.joystick.Joystick(0)

    joystick.init()

    # Set up a clock to control the loop speed
    clock = pygame.time.Clock()
    running: bool = True
    success: bool = True
    while running:
        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == JOYBUTTONDOWN:
                    print(f"Joystick button {event.button} pressed.")
                elif event.type == JOYBUTTONUP:
                    print(f"Joystick button {event.button} released.")
                elif event.type == JOYAXISMOTION:
                    # Check which axis was moved (x, y, or others)
                    axis = event.axis
                    value = event.value
                    print(f"Joystick axis {axis} moved to {value}.")
        except KeyboardInterrupt:
            running = False
            logger.warning("Ctrl+C, stopping...")
        except Exception as e:
            logger.error(e)
            running = False
            success = False

        clock.tick(60)

    pygame.quit()

    return success
