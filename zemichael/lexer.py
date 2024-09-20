from typing import Callable

from zemichael.datatypes.token import Token, TokenType


class Lexer:
    def __init__(self, source: str):
        self._source: str = source
        self._curr_position: int = -1
        self._peek_position: int = 0
        self._curr_char: str = ""

        self._read_char()

    def next_token(self) -> Token:
        self._skip_whitespace()
        if self._curr_char in ["=", "!"] and self._peek_char() in ["="]:
            token_literal = self._curr_char + self._peek_char()

            self._read_char()
            self._read_char()
            return Token(Token.Operators[token_literal], token_literal)

        if self._is_letter(self._curr_char):
            identifier = self._read_value(self._is_letter)
            token_type = Token.Keywords.get(identifier, TokenType.IDENT)
            return Token(token_type, identifier)

        if self._is_digit(self._curr_char):
            number = self._read_value(self._is_digit)
            return Token(TokenType.INT, number)

        if self._curr_position >= len(self._source):
            return Token(TokenType.EOF, "")

        token_type: TokenType = TokenType.ILLEGAL
        token_literal: str = self._curr_char
        if self._curr_char in Token.Characters:
            token_literal = self._curr_char
            token_type = Token.Characters[self._curr_char]

        self._read_char()
        return Token(token_type, token_literal)

    def _peek_char(self) -> str:
        return (
            self._source[self._peek_position]
            if self._peek_position < len(self._source)
            else ""
        )

    def _read_char(self):
        self._curr_char = (
            self._source[self._peek_position]
            if self._peek_position < len(self._source)
            else ""
        )
        self._curr_position, self._peek_position = (
            self._peek_position,
            self._peek_position + 1,
        )

    def _read_value(self, validation_fn: Callable) -> str:
        start = self._curr_position
        while validation_fn(self._curr_char):
            self._read_char()

        return self._source[start : self._curr_position]

    def _skip_whitespace(self) -> None:
        while self._curr_char in [" ", "\t", "\n", "\r"]:
            self._read_char()

    def _is_letter(self, char: str) -> bool:
        return char.isalpha() or char == "_"

    def _is_digit(self, char: str) -> bool:
        return char.isnumeric()
