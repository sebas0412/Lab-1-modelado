import Lexer
from Clases import Equation, MathExpression, MathRestriction
def parse_equation(equation):
    return Lexer.plyParse(equation)
def parse_restriction(restriction):
    return parse_equation(restriction)

def parse_problem(objective,restrictions, maximize):
    restrictionList = []
    for item in restrictions:
        restrictionList.insert(len(restrictionList), parse_restriction(item))
    for item in restrictionList:
        item.printEquation()



    tablaSimplex = [],[]
    varNames = []


parse_problem("30x1 + 100x2", ["-x1 + x2 <= 7", "4x1 + 10x2 <= 40", "10x1 >= 30"], True)



