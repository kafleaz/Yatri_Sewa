import re

# Define token patterns
token_specification = [
    ('NUMBER',    r'\d+(\.\d*)?'),  # Integer or decimal number
    ('ASSIGN',    r'='),            # Assignment operator
    ('END',       r';'),            # Statement terminator
    ('ID',        r'[A-Za-z]+'),    # Identifiers
    ('OP',        r'[+\-*/]'),      # Arithmetic operators
    ('SKIP',      r'[ \t]'),        # Skip over spaces and tabs
    ('MISMATCH',  r'.'),            # Any other character
]

# Compile the regex for performance
token_re = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
get_token = re.compile(token_re).match

# Token class to store token information
class Token:
    def __init__(self, type, value, position):
        self.type = type
        self.value = value
        self.position = position

    def __repr__(self):
        return f'Token({self.type}, {self.value}, {self.position})'

def lex(text):
    line_no = 1
    line_start = 0
    pos = 0
    tokens = []
    match = get_token(text)
    
    while match is not None:
        type = match.lastgroup
        value = match.group(type)
        
        if type == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif type == 'ID' and value in {'if', 'else', 'for', 'while'}:
            type = value.upper()
        elif type == 'SKIP':
            pos = match.end()
            match = get_token(text, pos)
            continue
        elif type == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_no}')
        
        tokens.append(Token(type, value, match.start()))
        pos = match.end()
        match = get_token(text, pos)

    tokens.append(Token('EOF', '', pos))
    return tokens

# Example usage
text = input('Enter the lexeme: ')
tokens = lex(text)
for token in tokens:
    print(token)
