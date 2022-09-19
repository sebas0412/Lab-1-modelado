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

dict = parse_equation("-3.8x1 + 5x2 -2x3")

for x in dict:
    print("Coeff: {}, Var: {}".format(x.coeff, x.variable))

