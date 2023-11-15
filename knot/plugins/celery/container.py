from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from .bus import MessageBus


class MessageBusContainer(DeclarativeContainer):
    messages = providers.Dependency()
    bus = providers.Singleton(
        MessageBus,
        messages=messages,
    )
