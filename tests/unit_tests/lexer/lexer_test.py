import pytest

from zemichael.lexer.lexer import Lexer
from zemichael.lexer.token import Token, TokenType


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        (
            "=+(){},;",
            [
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.PLUS, "+"),
                Token(TokenType.LPAREN, "("),
                Token(TokenType.RPAREN, ")"),
                Token(TokenType.LBRACE, "{"),
                Token(TokenType.RBRACE, "}"),
                Token(TokenType.COMMA, ","),
                Token(TokenType.SEMICOLON, ";"),
            ],
        ),
        (
            """
            let five = 5;
            let ten = 10;
            let add = fn(x, y) {
                x + y;
            };
            let result = add(five, ten);
            !-/*5;
            5 < 10 > 5;
            """,
            [
                Token(TokenType.LET, "let"),
                Token(TokenType.IDENT, "five"),
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.INT, "5"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.LET, "let"),
                Token(TokenType.IDENT, "ten"),
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.INT, "10"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.LET, "let"),
                Token(TokenType.IDENT, "add"),
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.FUNCTION, "fn"),
                Token(TokenType.LPAREN, "("),
                Token(TokenType.IDENT, "x"),
                Token(TokenType.COMMA, ","),
                Token(TokenType.IDENT, "y"),
                Token(TokenType.RPAREN, ")"),
                Token(TokenType.LBRACE, "{"),
                Token(TokenType.IDENT, "x"),
                Token(TokenType.PLUS, "+"),
                Token(TokenType.IDENT, "y"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.RBRACE, "}"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.LET, "let"),
                Token(TokenType.IDENT, "result"),
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.IDENT, "add"),
                Token(TokenType.LPAREN, "("),
                Token(TokenType.IDENT, "five"),
                Token(TokenType.COMMA, ","),
                Token(TokenType.IDENT, "ten"),
                Token(TokenType.RPAREN, ")"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.BANG, "!"),
                Token(TokenType.MINUS, "-"),
                Token(TokenType.SLASH, "/"),
                Token(TokenType.ASTERISK, "*"),
                Token(TokenType.INT, "5"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.INT, "5"),
                Token(TokenType.LT, "<"),
                Token(TokenType.INT, "10"),
                Token(TokenType.GT, ">"),
                Token(TokenType.INT, "5"),
                Token(TokenType.SEMICOLON, ";"),
            ],
        ),
        (
            "let x = 5;",
            [
                Token(TokenType.LET, "let"),
                Token(TokenType.IDENT, "x"),
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.INT, "5"),
                Token(TokenType.SEMICOLON, ";"),
            ],
        ),
        (
            "$5;",
            [
                Token(TokenType.ILLEGAL, "$"),
                Token(TokenType.INT, "5"),
                Token(TokenType.SEMICOLON, ";"),
            ],
        ),
        (
            """
            let five = 5;
            let ten = 10;
            let add = fn(x, y) {
                x + y;
            };

            let result = add(five, ten);

            !-/*5;
            5 < 10 > 5;

            if (5 < 10) {
                return true;
            } else {
                return false;
            }
            10 == 10;
            10 != 9;
            """,
            [
                Token(TokenType.LET, "let"),
                Token(TokenType.IDENT, "five"),
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.INT, "5"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.LET, "let"),
                Token(TokenType.IDENT, "ten"),
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.INT, "10"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.LET, "let"),
                Token(TokenType.IDENT, "add"),
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.FUNCTION, "fn"),
                Token(TokenType.LPAREN, "("),
                Token(TokenType.IDENT, "x"),
                Token(TokenType.COMMA, ","),
                Token(TokenType.IDENT, "y"),
                Token(TokenType.RPAREN, ")"),
                Token(TokenType.LBRACE, "{"),
                Token(TokenType.IDENT, "x"),
                Token(TokenType.PLUS, "+"),
                Token(TokenType.IDENT, "y"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.RBRACE, "}"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.LET, "let"),
                Token(TokenType.IDENT, "result"),
                Token(TokenType.ASSIGN, "="),
                Token(TokenType.IDENT, "add"),
                Token(TokenType.LPAREN, "("),
                Token(TokenType.IDENT, "five"),
                Token(TokenType.COMMA, ","),
                Token(TokenType.IDENT, "ten"),
                Token(TokenType.RPAREN, ")"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.BANG, "!"),
                Token(TokenType.MINUS, "-"),
                Token(TokenType.SLASH, "/"),
                Token(TokenType.ASTERISK, "*"),
                Token(TokenType.INT, "5"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.INT, "5"),
                Token(TokenType.LT, "<"),
                Token(TokenType.INT, "10"),
                Token(TokenType.GT, ">"),
                Token(TokenType.INT, "5"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.IF, "if"),
                Token(TokenType.LPAREN, "("),
                Token(TokenType.INT, "5"),
                Token(TokenType.LT, "<"),
                Token(TokenType.INT, "10"),
                Token(TokenType.RPAREN, ")"),
                Token(TokenType.LBRACE, "{"),
                Token(TokenType.RETURN, "return"),
                Token(TokenType.TRUE, "true"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.RBRACE, "}"),
                Token(TokenType.ELSE, "else"),
                Token(TokenType.LBRACE, "{"),
                Token(TokenType.RETURN, "return"),
                Token(TokenType.FALSE, "false"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.RBRACE, "}"),
                Token(TokenType.INT, "10"),
                Token(TokenType.EQ, "=="),
                Token(TokenType.INT, "10"),
                Token(TokenType.SEMICOLON, ";"),
                Token(TokenType.INT, "10"),
                Token(TokenType.NOT_EQ, "!="),
                Token(TokenType.INT, "9"),
                Token(TokenType.SEMICOLON, ";"),
            ],
        ),
    ],
)
def test_next_token(input, expected):
    # WHEN
    lexer = Lexer(input)

    # THEN
    for token in expected:
        next_token = lexer.next_token()
        print(next_token, token)
        assert next_token == token

    assert lexer.next_token() == Token(TokenType.EOF, "")
