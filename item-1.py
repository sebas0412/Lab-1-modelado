import Lexer
class MathExpression:
    variable = ""
    coeff = ""

class MathRestriction:
    restriction = ""
    type = ""

class Equation:
    # Lista para MathExpressions
    restrictionsList = []
    dictionary = []

    def insertExpression(self, item):
        self.dictionary.insert(len(self.dictionary), item)

    def insertRestriction(self, item):
        self.restrictionsList.insert(len(self.restrictionsList), item)

    def printEquation(self):
        print("\nMath expression:")
        for factor in self.dictionary:
            print("\tCoeff: {}, Variable: {}".format(factor.coeff, factor.variable))
        print("\nRestrictions:")
        for rest in self.restrictionsList:
            print("\tRestriction Type: {}, Restriction: {}".format(rest.type, rest.restriction))


def parse_equation(equation):
    Lexer.lexer.input(equation)
    thisEquation = Equation()
    thisItem = MathExpression()

    while True:
        tok = Lexer.lexer.token()

        if not tok:
            break
        if (tok.type == "COEFF"):
            thisItem.coeff = tok.value
            thisItem.coeff = thisItem.coeff.replace(' ', '')
        elif (tok.type == "VARIABLE"):
            thisItem.variable = tok.value
            thisEquation.insertExpression(thisItem)
            thisItem = MathExpression()

    return thisEquation

parse_equation("-3.8x1 + 5x2 -2x3").printEquation()

