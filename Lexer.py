import ply.lex as lex

tokens = (
    'COEFF',
    'VARIABLE',
    'OPERATOR',
)

t_COEFF = r'([\d]+)(?=[A-Za-z])'
t_VARIABLE = r'(\w{1}\d{1})'
t_OPERATOR = r'[+,-,*,/]'
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    exit()
    t.lexer.skip(1)

lexerData = ""
lexer = lex.lex()
lexer.input(lexerData)


# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)