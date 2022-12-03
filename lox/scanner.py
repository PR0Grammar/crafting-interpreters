from nis import match
import lox.lox as lox
from lox.token import Token
from lox.token_type import TokenType


class Scanner:
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    # Main method handling the scan
    def scan_tokens(self):
        while not self.is_at_end():
            # Start of "substr" of the current scan
            self.start = self.current
            self.scan_token()
            self.current += 1

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    # Determine if we cannot scan anymore chars
    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def scan_token(self):
        c = self.get_char()

        ############## Strictly single char checks #############
        if c == "(":
            self.add_token(TokenType.LEFT_PAREN)
        elif c == ")":
            self.add_token(TokenType.RIGHT_PAREN)
        elif c == "{":
            self.add_token(TokenType.LEFT_BRACE)
        elif c == "}":
            self.add_token(TokenType.RIGHT_BRACE)
        elif c == ",":
            self.add_token(TokenType.COMMA)
        elif c == ".":
            self.add_token(TokenType.DOT)
        elif c == "-":
            self.add_token(TokenType.MINUS)
        elif c == "+":
            self.add_token(TokenType.PLUS)
        elif c == ";":
            self.add_token(TokenType.SEMICOLON)
        elif c == "-":
            self.add_token(TokenType.MINUS)
        elif c == "*":
            self.add_token(TokenType.STAR)
        ############## Single or double char checks #############
        elif c == "!":
            self.add_token(TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG)
        elif c == "=":
            self.add_token(
                TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL
            )
        elif c == "<":
            self.add_token(TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS)
        elif c == ">":
            self.add_token(
                TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER
            )
        ############## Literals #############
        # String literal
        elif c == '"':
            while self.peek() != '"' and not self.is_at_end():
                if self.peek() == "\n":
                    self.line += 1
                self.current += 1

            if self.is_at_end():
                lox.error(self.line, "Unterminated string")

            # Increment to the closing quote
            self.current += 1

            str_literal = self.source[self.start + 1 : self.current]
            self.add_token(TokenType.STRING, str_literal)
        elif c.isnumeric():
            decimal_seen = False
            while self.peek != "\n" and not self.is_at_end():
                if self.peek() == ".":
                    if decimal_seen:
                        lox.error(self.line, "Unexpected character in number literal.")
                    else:
                        decimal_seen = True
                elif not self.peek().isnumeric():
                    lox.error(self.line, "Unexpected character in number literal.")
                self.current+=1

            num_literal_str = self.source[self.start:self.current+1]
            num_literal = float(num_literal_str) if decimal_seen else int(num_literal_str) 
            self.add_token(TokenType.NUMBER, num_literal)
        ############## Special cases #############
        elif c == "/":
            # Comments - keep going until end of line or self of file
            if self.match("/"):
                while self.peek() != "\n" and not self.is_at_end():
                    self.current += 1
            else:
                # Otherwise, its division
                self.add_token(TokenType.SLASH)
        elif c == "\n":
            self.line += 1
        ############## Cases to ignore - whitespace #############
        elif c == " " or c == "\r" or c == "\t":
            return
        ############## Default - error out #############
        else:
            lox.error(self.line, "Unexpected character.")

    # Get the current character to evaluate
    def get_char(self) -> str:
        return self.source[self.current]

    # Peek at the next character without incrementing position
    def peek(self) -> str:
        if self.is_at_end():
            return "\0"
        return self.source[self.current + 1]

    # Adds the next Token with its metadata to the Token list
    def add_token(self, token_type: TokenType, literal):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    # Returns true and increments current char pointer if the next char is the expected char
    def match(self, expected_char) -> bool:
        if self.is_at_end():
            return False

        maybe_next_char = self.source[self.current + 1]
        if maybe_next_char == expected_char:
            self.current += 1
            return True
        return False
