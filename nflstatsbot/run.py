import logging
from query import StatQuery


def run_bot(text_input):
    query = StatQuery(text_input)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    user_input = input('Enter an NFL stat query: ')
    run_bot(user_input)
