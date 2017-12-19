import logging.config

from nflstatsbot import load_config, StatQuery


def run_bot(text_input):
    return StatQuery(text_input)


if __name__ == '__main__':
    log_cfg = load_config('logging.yml', 'LOG_CFG')
    logging.config.dictConfig(log_cfg)
    user_input = input('Enter an NFL stat query: ')
    run_bot(user_input)
