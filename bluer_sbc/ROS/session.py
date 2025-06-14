import time
import RPi.GPIO as GPIO  # type: ignore

from blueness import module

from bluer_sbc import NAME
from bluer_sbc.ROS.pre.session import PreROSSession
from bluer_sbc.session.functions import reply_to_bash
from bluer_sbc.logger import logger

NAME = module.name(__file__, NAME)


def start_session() -> bool:
    logger.info(f"{NAME}.start_session.")

    session = PreROSSession()

    if not session.initialize():
        return False

    try:
        while not (session.button_command() or session.key_command()):
            session.leds.update()
            time.sleep(0.05)
    except KeyboardInterrupt:
        logger.info("^C received.")
        return False
    finally:
        GPIO.cleanup()

    return True
