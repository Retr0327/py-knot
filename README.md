# py-knot

This repository offers a message bus system tailored for integration with [python-dependency-injector
](https://github.com/ets-labs/python-dependency-injector/tree/master). It efficiently manages command and query dispatching and supports dependency injection, enhancing application decoupling, organization, and maintainability.

## **Installation**

The source code is currently hosted on GitHub at: https://github.com/Retr0327/py-knot

Binary installers for the latest released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/py-knot/).

- pip

  ```bash
  pip install pyknot
  ```

- poetry
  ```bash
  poetry add pyknot
  ```

## **Usage**

### 1. Fundamental Implementation

1. Define messages:

   Create specific command or query messages by extending `Command` or `Query` classes.

   ```python
   from dataclasses import dataclass
   from knot import Command

   ReturnType = dict[str, int]


   @dataclass(slots=True)
   class TestCommand(Command[ReturnType]):
       a: int
       b: int
   ```

2. Define handlers:

   Implement `CommandHandler` or `QueryHandler` for handling defined messages.

   ```python
   from dataclasses import dataclass
   from knot import Command, CommandHandler

   ReturnType = dict[str, int]


   @dataclass(slots=True)
   class TestCommand(Command[ReturnType]):
       a: int
       b: int


   class TestCommandHandler(CommandHandler[TestCommand]):
       def handle(self, message: TestCommand) -> ReturnType:
           return message.as_dict()
   ```

### 2. Integration with Dependency Injection

### 3. Extension as a Celery Plugin

## Contact Me

If you have any suggestion or question, please do not hesitate to email me at retr0327.dev@gmail.com.
