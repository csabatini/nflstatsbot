import logging
import os
from os.path import dirname, join
from typing import Any, Dict

import yaml


log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)


def load_config(file_name: str, env_key: str) -> Dict[str, Any]:
    """Utility function to parse a YAML configuration file"""
    logger = logging.getLogger(__name__)
    module_dir = dirname(__file__)
    file_path = os.getenv(env_key, None) or join(module_dir, file_name)

    try:
        logger.info(f'Loading configuration from file: {file_path}')
        with open(file_path, 'r') as f:
            return yaml.safe_load(f.read())
    except (OSError, IOError) as e:
        logger.exception(f'Failed to read configuration file: {file_path}', e)
        return dict()
