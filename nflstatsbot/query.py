import logging
import re
from enum import Enum, auto

QUERY_PATTERN = '^[a-zA-Z\s]{3,}$'


class StatQuery(object):
    """Representation of a user submitted statistic query"""
    class Type(Enum):
        """Type of query submitted by the user"""
        none = auto()
        malformed = auto()
        player = auto()

    def __init__(self, query_text: str) -> None:
        self._query_text = query_text
        self._query_type = StatQuery.Type.none if re.match(
            QUERY_PATTERN, self.query_text) is None else StatQuery.Type.player
        logging.debug(f'Query created: {self.query_type}')

    @property
    def query_text(self) -> str:
        """The text content of the query"""
        return self._query_text

    @property
    def query_type(self) -> Type:
        """The type of user query: one of none, malformed, player"""
        return self._query_type
