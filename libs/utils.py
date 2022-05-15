from logging import Logger, getLogger
from logging.config import fileConfig
from pathlib import Path
from typing import Final, Union

LOGGER_NAME: Final[str] = ""


def get_logger(conf_path: Union[Path, str]) -> Logger:
    if not Path(conf_path).exists():
        raise FileNotFoundError(f"{conf_path} does not exist")
    elif not Path(conf_path).is_file():
        raise FileExistsError(f"{conf_path} is not a file")

    fileConfig(conf_path)
    logger: Logger = getLogger(LOGGER_NAME)
    logger.info("logger init")
    return logger
