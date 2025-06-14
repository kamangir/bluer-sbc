import keyboard
import time
import RPi.GPIO as GPIO  # type: ignore

from blueness import module
from bluer_options import string

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

button = {"pin": 26, "state": False}

leds = {
    "yellow": {"pin": 17, "state": True},
    "red": {"pin": 27, "state": False},
    "green": {"pin": 22, "state": True},
}

BUTTON_PRESS_DURATION_UPDATE = 5
BUTTON_PRESS_DURATION_SHUTDOWN = 10


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
        GPIO.setup(
            button["pin"],
            GPIO.IN,
            pull_up_down=GPIO.PUD_UP,
        )
        for led in leds.values():
            GPIO.setup(
                led["pin"],
                GPIO.OUT,
            )
    except Exception as e:
        logger.error(e)
        return False

    exit_flag: bool = False
    button_press_time: int = 0
    button_press_duration: int = -1
    try:
        while not exit_flag:
            for key, event in bash_keys.items():
                if keyboard.is_pressed(key):
                    reply_to_bash(event)
                    exit_flag = True
                    break

            button_pressed = not GPIO.input(button["pin"])
            if button_pressed:
                if not button["state"]:
                    logger.info("button pressed.")
                    button_press_time = time.time()

                button_press_duration = time.time() - button_press_time
                if button_press_duration > BUTTON_PRESS_DURATION_SHUTDOWN:
                    leds["red"]["state"] = True
                elif button_press_duration > BUTTON_PRESS_DURATION_UPDATE:
                    leds["red"]["state"] = not leds["red"]["state"]
            else:
                if button["state"]:
                    logger.info(
                        "button released after {}.".format(
                            string.pretty_duration(
                                button_press_duration,
                            )
                        )
                    )
                if button_press_duration > BUTTON_PRESS_DURATION_SHUTDOWN:
                    reply_to_bash("shutdown")
                    exit_flag = True
                elif button_press_duration > BUTTON_PRESS_DURATION_UPDATE:
                    reply_to_bash("update")
                    exit_flag = True

            button["state"] = button_pressed

            leds["yellow"]["state"] = button["state"]

            leds["green"]["state"] = not leds["green"]["state"]

            for led in leds.values():
                GPIO.output(
                    led["pin"],
                    GPIO.HIGH if led["state"] else GPIO.LOW,
                )

            time.sleep(0.05)
    except KeyboardInterrupt:
        logger.info("^C received.")
        return False
    finally:
        GPIO.cleanup()

    return True
