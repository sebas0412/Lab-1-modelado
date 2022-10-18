class MathExpression:
    variable = ""
    coeff = ""

class MathRestriction:
    value = ""
    type = ""

class Equation:
    # Lista para MathExpressions
    restriction = MathRestriction()
    dictionary = []
    def __init__(self):
        self.dictionary = []
        self.restriction = MathRestriction()


    def insertExpression(self, item):
        self.dictionary.insert(len(self.dictionary), item)

    def printEquation(self):
        print("\nMath expression:")
        for factor in self.dictionary:
            print("\tCoeff: {}, Variable: {}".format(factor.coeff, factor.variable))
        print("Restriction:")
        print("\tRestriction Type: {}, Restriction: {}\n".format(self.restriction.type, self.restriction.value))