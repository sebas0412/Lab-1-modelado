import Lexer
import numpy as np
from numpy import linalg as lina
from numpy.linalg import inv
from Clases import Equation, MathExpression, MathRestriction


def parse_equation(equation):
    thisEquation = Lexer.plyParse(equation)
    dictionary = {}

    for item in thisEquation.dictionary:
        dictionary[item.coeff] = item.variable.replace('+', '')
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

    objArray = []
    varArray = []


    for var in parsedObjective:
        objArray.insert(len(objArray), var)

    for index in range (0, len(restrictions)):
        objArray.insert(len(objArray), 0)

    if (False in rest_upperBound):
        objArray.insert(len(objArray), -100000.0)

    restColumns = len(rest_dictionary) + len(parsedObjective) + 1
    if(False in rest_upperBound):
        restColumns += 1

    restMatrix = np.zeros((len(rest_dictionary), restColumns))

    for i in range(0, len(restMatrix[:, 0])):
        for j in range(0, len(parsedObjective)):
            iter = 0
            restMatrix[i, j] = get_nth_key(rest_dictionary[i], j)

    objectiveNump = np.array(objArray)



# Se crea una tabla vacia, con suficientes filas y columnas para abarcar las variables y restricciones
def generateMatrix(variables, constraints):
    table = np.zeros((constraints + 1, variables + constraints + 2))
    return table

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")

parse_problem("30x1 + 100x2", ["x1 + x2 <= 7", "4x1 + 10x2 <= 40", "10x1 >= 30"], True)
