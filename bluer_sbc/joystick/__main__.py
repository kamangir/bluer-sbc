import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_sbc import NAME
from bluer_sbc.joystick.validation import validate
from bluer_sbc.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="validate",
)
args = parser.parse_args()

success = False
if args.task == "validate":
    success = validate()
else:
    success = None

sys_exit(logger, NAME, args.task, success)
