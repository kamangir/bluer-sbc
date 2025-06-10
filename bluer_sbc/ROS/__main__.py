import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_sbc import NAME
from bluer_sbc.logger import logger
from bluer_sbc.ROS.session import start_session

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="start_session",
)
args = parser.parse_args()

success = False
if args.task == "task":
    success = start_session()
else:
    success = None
sys_exit(logger, NAME, args.task, success)
