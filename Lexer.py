from time import sleep

import ply.lex as lex
import ply.yacc as yacc
from Clases import Equation, MathExpression, MathRestriction

equation = Equation()

tokens = (
    'STARTING_COEFF',
    'STARTING_COEFF_EMPTY',
    'NORMAL_COEFF',
    'EMPTY_COEFF',
    'FRACTION_COEFF',

    'COEFF',

    'STARTING_VARIABLE',
    'VARIABLE',
    'BOUND',
    'RESTRICTION',
    'GARBAGE',
)

t_STARTING_COEFF = r'^[\+\-\*\/]?\s?[0-9]+(?=(\w\d))'
t_STARTING_COEFF_EMPTY = r'^[\+\-\*\/]?\s?(?=([A-Za-z][0-9]))'
t_NORMAL_COEFF = r'[\+\-\*\/]\s?([0-9]+)(?=([A-Za-z][0-9]))'
t_EMPTY_COEFF = r'[\+\-\*\/]\s?(?=([A-Za-z][0-9]))'
t_FRACTION_COEFF = r'[\+\-\*\/]?\s?([0-9]+\.[0-9]+)(?=([A-Za-z][0-9]))'

t_VARIABLE = r'([A-Za-z][0-9])'
t_STARTING_VARIABLE = r'^([A-Za-z][0-9])'
t_BOUND = r'((?<=.)(<=|>=))'
t_RESTRICTION = r'((?<=(<=|>=)\s)\d+)'
t_GARBAGE = r'.+'
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    exit()
    t.lexer.skip(1)

#######################################################################################################################
def p_error(t):
    print("Syntax error at '%s'" % t.value)

def p_equation(t):
    '''equation :   expression BOUND RESTRICTION
                |   expression'''
    try:
        equation.restriction.type = t[2]
        equation.restriction.value = t[3]
    except:
        print("This equation presents no restriction")
def p_expression(t):
    '''expression :     expression factor
                  |     factor'''

def p_factor(t):
    '''factor   :   startingcoeff VARIABLE
                |   startingcoeffempty VARIABLE
                |   normalcoeff VARIABLE
                |   emptycoeff VARIABLE
                |   fractioncoeff VARIABLE
                |   STARTING_VARIABLE'''
    try:
        item = MathExpression()
        item.coeff = t[1]
        item.variable = t[2]
        equation.insertExpression(item)
        t[0] = t[1] + t[2]
    except:
        print("DASDAS")
        item = MathExpression()
        item.coeff = "1"
        item.variable = t[1]
        equation.insertExpression(item)
        t[0] = t[1]


#######################################################################################################################

def p_startingcoeff(t):
    '''startingcoeff    :   STARTING_COEFF'''
    t[0] = t[1]
def p_startingcoeffempty(t):
    '''startingcoeffempty   :   STARTING_COEFF_EMPTY'''
    t[0] = t[1]
def p_normalcoeff(t):
    '''normalcoeff  :   NORMAL_COEFF'''
    t[0] = t[1]
def p_emptycoeff(t):
    '''emptycoeff   :   EMPTY_COEFF'''
    t[0] = t[1]
def p_fractioncoeff(t):
    '''fractioncoeff    :   FRACTION_COEFF'''
    t[0] = t[1]

#######################################################################################################################


def plyParse(data):
    lexer = lex.lex()
    parser = yacc.yacc()
    equation = Equation()
    parser.parse(data)
    return equation
