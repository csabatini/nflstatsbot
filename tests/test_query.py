from nflstatsbot.query import StatQuery


def test_valid_query_types():
    query_inputs = ['DeMarco Murray',
                    'Dez Bryant',
                    'Antonio Brown']

    query_outputs = [StatQuery(i) for i in query_inputs]
    assert len(query_outputs) == len(query_inputs)

    for query in query_outputs:
        assert query is not None
        assert isinstance(query, StatQuery)
        assert query.query_type == StatQuery.Type.player


def test_invalid_query_types():
    # TODO: account for valid special characters in names
    query_inputs = [']Calvin Johnson',
                    'A.J. Green',
                    'Todd $@^&*___!$@# Gurley',
                    'Adrian \'All Day\' Peterson']

    query_outputs = [StatQuery(i) for i in query_inputs]
    assert len(query_outputs) == len(query_inputs)

    for query in query_outputs:
        assert query is not None
        assert isinstance(query, StatQuery)
        assert query.query_type == StatQuery.Type.none
