import pytest

from knot.types import MessageHandler

from .mocks import (
    MockCommand,
    MockCommandHandler,
    MockQuery,
    MockQueryHandler,
)


@pytest.fixture
def mock_message_handlers() -> list[MessageHandler]:
    return [MockQueryHandler(), MockCommandHandler()]


def test_message_handler_types(mock_message_handlers: list[MessageHandler]):
    assert all(
        issubclass(type(message_handler), MessageHandler)
        for message_handler in mock_message_handlers
    )


def test_message_handler_handle_method(mock_message_handlers: list[MessageHandler]):
    actual = {"a": 1}
    assert all(
        message_handler.handle(message) == actual
        for message_handler, message in zip(
            mock_message_handlers, [MockQuery(), MockCommand()], strict=True
        )
    )
