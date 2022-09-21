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

    def insertExpression(self, item):
        self.dictionary.insert(len(self.dictionary), item)

    def printEquation(self):
        print("\nMath expression:")
        for factor in self.dictionary:
            print("\tCoeff: {}, Variable: {}".format(factor.coeff, factor.variable))
        print("\nRestriction:")
        print("\tRestriction Type: {}, Restriction: {}".format(self.restriction.type, self.restriction.value))