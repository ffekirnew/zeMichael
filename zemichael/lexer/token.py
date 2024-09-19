import enum


class TokenType(enum.Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"

    # Identifiers + literals
    IDENT = "IDENT"  # add, foobar, x, y, ...
    INT = "INT"  # 1343456

    # Operators
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"

    LT = "<"
    GT = ">"
    EQ = "=="
    NOT_EQ = "!="

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"


class Token:
    Keywords: dict[str, TokenType] = {
        "let": TokenType.LET,
        "fn": TokenType.FUNCTION,
        "true": TokenType.TRUE,
        "false": TokenType.FALSE,
        "if": TokenType.IF,
        "else": TokenType.ELSE,
        "return": TokenType.RETURN,
    }

    Operators: dict[str, TokenType] = {
        "+": TokenType.PLUS,
        "-": TokenType.MINUS,
        "!": TokenType.BANG,
        "/": TokenType.SLASH,
        "*": TokenType.ASTERISK,
        "<": TokenType.LT,
        ">": TokenType.GT,
        "=": TokenType.ASSIGN,
        "==": TokenType.EQ,
        "!=": TokenType.NOT_EQ,
    }

    Delimiters: dict[str, TokenType] = {
        ";": TokenType.SEMICOLON,
        "(": TokenType.LPAREN,
        ")": TokenType.RPAREN,
        ",": TokenType.COMMA,
        "{": TokenType.LBRACE,
        "}": TokenType.RBRACE,
    }

    Characters: dict[str, TokenType] = {
        **Keywords,
        **Operators,
        **Delimiters,
    }

    def __init__(self, token_type: TokenType, litral: str) -> None:
        self._type: TokenType = token_type
        self._literal: str = litral

    def __repr__(self) -> str:
        return f"Token ({self._type}, '{self._literal}')"

    def __eq__(self, other: object, /) -> bool:
        return (self._type.value, self._literal) == (other._type.value, other._literal)
