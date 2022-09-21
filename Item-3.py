import Lexer

class Item:
    variable = ""
    coeff = ""


def parse_equation(equation):
    dictionary = []

    Lexer.lexer.input(equation)
    thisItem = Item()

    while True:
        tok = Lexer.lexer.token()

        if not tok:
            break
        if (tok.type == "COEFF"):
            thisItem.coeff = tok.value
        elif (tok.type == "VARIABLE"):
            thisItem.variable = tok.value
            dictionary.insert(len(dictionary), thisItem)
            thisItem = Item()

    return dictionary

def parse_restriction(restriction):
    bound = ""
    Lexer.lexer.input(restriction)
    thisItem = Item()

    while True:
        tok = Lexer.lexer.token()
        if not tok:
            break
        if (tok.type == "BOUND"):
            thisItem.bound = tok.value
            bound = thisItem.bound
        if (tok.type == "RESTRICTION"):
            thisItem.restriction = tok.value
            restriction = thisItem.restriction
            thisItem = Item()
    dict = parse_equation("-3.8x1 + 5x2 -2x3")
    for x in dict:
        print("{} : {}, ".format(x.variable, x.coeff), end = " ")
    if (bound == "<="):
        print("Upper bound")
    elif(bound == ">="):
        print("Lower bound")
    print("Restriction: ", restriction)
    return restriction

def parse_problem(objective,restrictions, maximize):
    coeficientes = []
    tablaSimplex = [],[]
    varNames = []

    return coeficientes,tablaSimplex,varNames

str = parse_restriction("-3.8x1 + 5x2 - 2x3 <= 35")



