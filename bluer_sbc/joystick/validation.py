from blueness import module

from bluer_sbc import NAME
from bluer_sbc.logger import logger


NAME = module.name(__file__, NAME)


def validate() -> bool:
    logger.info(f"{NAME}.validate")
    return True
