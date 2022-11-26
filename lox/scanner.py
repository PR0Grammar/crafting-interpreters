from lox.token import Token
from lox.token_type import TokenType


class Scanner:
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def scan_token(self):
        c = self.next_ch()

        if(c == '('):
            self.add_token(TokenType.LEFT_PAREN)
        elif(c == ')'):
            self.add_token(TokenType.RIGHT_PAREN)
        elif(c == '{'):
            self.add_token(TokenType.LEFT_BRACE)
        elif(c == '}'):
            self.add_token(TokenType.RIGHT_BRACE)
        elif(c == ','):
            self.add_token(TokenType.COMMA)
        elif(c == '.'):
            self.add_token(TokenType.DOT)
        elif(c == '-'):
            self.add_token(TokenType.MINUS)
        elif(c == '+'):
            self.add_token(TokenType.PLUS)
        elif(c == ';'):
            self.add_token(TokenType.SEMICOLON)
        elif(c == '-'):
            self.add_token(TokenType.MINUS)
        elif(c == '*'):
            self.add_token(TokenType.STAR)

    def next_ch(self):
        self.current+=1
        return self.source[self.current - 1]
    
    def add_token(self, token_type: TokenType, literal):
        text = self.source[self.start: self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))
