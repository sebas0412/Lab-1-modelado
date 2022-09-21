import Lexer
from Clases import Equation, MathExpression, MathRestriction
def parse_equation(equation):
    return Lexer.plyParse(equation)
def parse_restriction(restriction):
    return parse_equation(restriction)

def parse_problem(objective,restrictions, maximize):
    restrictionList = []
    eq = parse_equation(objective)
    for item in restrictions:
        restrictionList.insert(0, parse_restriction(item))


    tablaSimplex = [],[]
    varNames = []


parse_problem("30x1 + 100x2", ["10x1 <= 10", "20x2 <= 20"], True)



