import ply.lex as lex

tokens = (
    'COEFF',
    'VARIABLE',
    'BOUND',
    'RESTRICTION',
    'GARBAGE',
)

t_COEFF = r'([\+\-\*\/])(\s?)(\d)(\.?\d?)'
t_VARIABLE = r'(\w{1}\d{1})'
t_BOUND = r'((?<=.)(<=|>=))'
t_RESTRICTION = r'((?<=(<=|>=)\s)\d+)'
t_ignore = ' \t'
t_GARBAGE = r'.+'

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

###################################################################################################################
