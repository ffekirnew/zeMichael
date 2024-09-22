from zemichael.datatypes.ast import (
    BlockStatement,
    Expression,
    Identifier,
    IfStatement,
    LetStatement,
    Program,
    ReturnStatement,
    Statement,
)
from zemichael.datatypes.token import Token, TokenType
from zemichael.lexer import Lexer


class Parser:
    def __init__(self, lexer: Lexer) -> None:
        self._lexer: Lexer = lexer
        self._curr_token: Token
        self._peek_token: Token

        self._advance_tokens()
        self._advance_tokens()

    def parse(self) -> Program:
        statements: list[Statement] = []

        while self._curr_token.token_type != TokenType.EOF:
            if self._curr_token.token_type == TokenType.LET:
                statements.append(self._parse_let_statement())
            if self._curr_token.token_type == TokenType.RETURN:
                statements.append(self._parse_return_statement())
            if self._curr_token.token_type == TokenType.IF:
                statements.append(self._parse_if_statement())

            self._advance_tokens()

        return Program(statements)

    def _advance_tokens(self) -> None:
        self._curr_token, self._peek_token = self._peek_token, self._lexer.next_token()

    def _parse_let_statement(self) -> LetStatement:
        """let <name> = <expression>;"""
        let_token: Token = self._curr_token
        self._advance_tokens()
        name_token: Token = self._curr_token
        self._advance_tokens()
        self._advance_tokens()
        expression = self._parse_expression()

        name: Identifier = Identifier()
        name.token = name_token

        statement = LetStatement()
        statement.token = let_token
        statement.name = name
        statement.value = expression

        return statement

    def _parse_return_statement(self) -> ReturnStatement:
        """return <expression>;"""
        statement = ReturnStatement()

        statement.token = self._curr_token
        statement.value = self._parse_expression()

        return statement

    def _parse_if_statement(self) -> IfStatement:
        """if (<condition>) {<consequence>} else {<alternative>}"""
        statement = IfStatement()

        statement.token = self._curr_token

        self._advance_tokens()
        self._advance_tokens()

        statement.condition = self._parse_expression()

        self._advance_tokens()
        self._advance_tokens()

        statement.consequence = self._parse_block_statement()

        if self._peek_token.token_type == TokenType.ELSE:
            self._advance_tokens()
            self._advance_tokens()

            statement.alternative = self._parse_block_statement()

        return statement

    def _parse_expression(self) -> Expression: ...
    def _parse_block_statement(self) -> BlockStatement: ...
