import pytest

from knot.types import Message

from .mocks import (
    MockCommand,
    MockQuery,
)


@pytest.fixture
def mock_messages() -> list[Message]:
    return [MockQuery(), MockCommand()]


def test_message_types(mock_messages: list[Message]):
    assert all(issubclass(type(message), Message) for message in mock_messages)


def test_message_as_dict_method(mock_messages: list[Message]):
    actual = {"a": 1}
    assert all(message.as_dict() == actual for message in mock_messages)
