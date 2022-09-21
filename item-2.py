import Lexer
from Clases import Equation, MathExpression, MathRestriction
def parse_equation(equation):
    return Lexer.plyParse(equation)
def parse_restriction(restriction):
    return parse_equation(restriction)

parse_restriction("-3.8x1 + 5x2 - 2x3 <= 35").printEquation()



