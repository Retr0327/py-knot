from dependency_injector.providers import Factory
import pytest

from knot import register_handlers
from knot.plugins.di import handlers_to_factories

from .mocks import (
    MockCommand,
    MockCommandHandler,
    MockQuery,
    MockQueryHandler,
)


@pytest.fixture
def mock_handler_factory():
    return register_handlers((MockQueryHandler, MockCommandHandler))


def test_handler_registration(mock_handler_factory):
    assert mock_handler_factory[MockQuery] == MockQueryHandler
    assert mock_handler_factory[MockCommand] == MockCommandHandler

    with pytest.raises(AssertionError):
        assert mock_handler_factory[MockQuery] == MockCommandHandler
        assert mock_handler_factory[MockCommand] == MockQueryHandler


def test_provider_factory(mock_handler_factory):
    provider_factory = handlers_to_factories(mock_handler_factory)
    assert all(
        isinstance(provider_factory[message_type], Factory)
        for message_type in (MockQuery, MockCommand)
    )
