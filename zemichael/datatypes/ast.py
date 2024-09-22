from abc import ABCMeta, abstractmethod

from zemichael.datatypes.token import Token


class Node(metaclass=ABCMeta):
    @abstractmethod
    def token_literal(self) -> str: ...


class Statement(Node, metaclass=ABCMeta): ...


class Expression(Node, metaclass=ABCMeta): ...


class Program(Node):
    def __init__(self, statements: list[Statement]):
        self._statements: list[Statement] = statements

    @property
    def statements(self):
        return self._statements

    def token_literal(self) -> str:
        if len(self._statements) > 0:
            return self._statements[0].token_literal()

        return ""


class Identifier(Expression):
    def __init__(self):
        self.token: Token
        self.value: str

    def token_literal(self) -> str:
        return self.token.literal


class LetStatement(Statement):
    def __init__(self):
        self.token: Token
        self.name: Identifier
        self.value: Expression

    def token_literal(self) -> str:
        return self.token.literal


class IfStatement(Statement):
    def __init__(self):
        self.token: Token
        self.condition: Expression
        self.consequence: BlockStatement
        self.alternative: BlockStatement

    def token_literal(self) -> str:
        return self.token.literal


class ReturnStatement(Statement):
    def __init__(self):
        self.token: Token
        self.value: Expression

    def token_literal(self) -> str:
        return self.token.literal


class BlockStatement(Statement):
    def __init__(self):
        self.token: Token
        self.statements: list[Statement]

    def token_literal(self) -> str:
        return self.token.literal
