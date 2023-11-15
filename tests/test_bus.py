import pytest

from knot import (
    MessageBus,
    register_handlers,
)

from .mocks import (
    MockCommand,
    MockCommandHandler,
    MockQuery,
    MockQueryHandler,
)


@pytest.fixture
def mock_message_bus():
    messages = register_handlers((MockQueryHandler, MockCommandHandler))
    return MessageBus(messages=messages)


def test_dispatch(mock_message_bus):
    actual = {"a": 1}

    assert mock_message_bus.dispatch(MockQuery()) == actual
    assert mock_message_bus.dispatch(MockCommand()) == actual

    del mock_message_bus.messages[MockQuery]
    with pytest.raises(ValueError):
        assert mock_message_bus.dispatch(MockQuery()) == actual
