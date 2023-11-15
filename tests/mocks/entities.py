from dataclasses import dataclass

from knot.types import (
    Command,
    CommandHandler,
    Query,
    QueryHandler,
)

MockReturnType = dict[str, int]


@dataclass(slots=True)
class MockQuery(Query[MockReturnType]):
    a: int = 1


class MockQueryHandler(QueryHandler[MockQuery]):
    def handle(self, message: MockQuery) -> MockReturnType:
        return message.as_dict()


@dataclass(slots=True)
class MockCommand(Command[MockReturnType]):
    a: int = 1


class MockCommandHandler(CommandHandler[MockCommand]):
    def handle(self, message: MockCommand) -> MockReturnType:
        return message.as_dict()
