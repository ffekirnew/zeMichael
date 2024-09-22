import pytest

from zemichael.lexer import Lexer
from zemichael.parser import Parser


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        (
            """
            let five = 5;
            let ten = 10;
            """,
            [],
        ),
    ],
)
def test_next_token(input, expected):
    # WHEN
    lexer = Lexer(input)
    parser = Parser(lexer)

    program = parser.parse()

    # THEN
    assert len(program.statements) == 2
    assert program.statements[0].token_literal() == "let"
