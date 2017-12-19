import os
from os.path import dirname, join

import nflstatsbot
from nflstatsbot import load_config

EXPECTED_LOG_HANDLERS = {
    'console': {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG',
        'formatter': 'simple',
        'stream': 'ext://sys.stdout'
    }
}

EXPECTED_POSTGRES_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'db': 'nfldb',
    'user': 'postgres',
    'password': 'local'
}


def test_loads_config_from_default_path():
    result = load_config('logging.yml', 'LOG_CFG')

    assert isinstance(result, dict)
    assert 'handlers' in result
    assert result['handlers'] == EXPECTED_LOG_HANDLERS


def test_loads_config_from_env_variable():
    os.environ['BOT_CFG'] = \
        join(dirname(nflstatsbot.__file__), 'botconfig.yml')

    # env variable path should be loaded instead of config file in module
    result = load_config('logging.yml', 'BOT_CFG')

    assert isinstance(result, dict)
    assert 'postgresql' in result
    assert result['postgresql'] == EXPECTED_POSTGRES_CONFIG


def test_load_failure_returns_empty_config():
    result = load_config('missing.yml', 'LOG_CFG')

    assert isinstance(result, dict)
    assert result == {}
