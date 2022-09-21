import Lexer
from Clases import Equation, MathExpression, MathRestriction
def parse_equation(equation):
    return Lexer.plyParse(equation)

parse_equation("-3.8x1 + 5x2 -2x3").printEquation()

