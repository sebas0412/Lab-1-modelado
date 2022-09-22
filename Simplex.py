import Lexer
import numpy as nump
from numpy import linalg as lina
from numpy.linalg import inv
from Clases import Equation, MathExpression, MathRestriction


def parse_equation(equation):
    thisEquation = Lexer.plyParse(equation)
    dictionary = {}

    for item in thisEquation.dictionary:
        dictionary[item.coeff] = item.variable
    return dictionary


def parse_restriction(restriction):
    thisEquation = Lexer.plyParse(restriction)
    dictionary = {}
    isUpperBound = False

    for item in thisEquation.dictionary:
        dictionary[item.coeff] = item.variable

    if (thisEquation.restriction.type == "<="):
        isUpperBound = True
    return dictionary, thisEquation.restriction.value, isUpperBound


def parse_problem(objective, restrictions, maximize):
    parsedObjective = parse_equation(objective)

    rest_dictionary = []
    rest_value = []
    rest_upperBound = []

    for index in range(0, len(restrictions)):
        dictionary, restrictionValue, isUpperBound = parse_restriction(restrictions[index])

        rest_dictionary.insert(index, dictionary)
        rest_value.insert(index, restrictionValue)
        rest_upperBound.insert(index, isUpperBound)

    tablaSimplex = [], []
    varNames = []


parse_problem("30x1 + 100x2", ["-x1 + x2 <= 7", "4x1 + 10x2 <= 40", "10x1 >= 30"], True)
