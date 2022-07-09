from abc import ABC


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class Checarsaldo(Command):

    def __init__(self, saldo: str) -> None:
        self._saldo = saldo

    def execute(self) -> None:


class Checarextratos(Command):

    def __init__(self, extratos: str) -> None:
        self._extratos = extratos

    def execute(self) -> None:


class CommandHistory:
    private field history: array of Command

    method push(c: Command):

    method pop(): Command:
