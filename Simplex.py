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
            ##restMatrix[i, j] = get_nth_key(rest_dictionary[i], j)

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

def columnaPivote(objective):
    columnaPivote = np.argmin(objective)
    return columnaPivote


def filaPivote(restrictions,cPivot):
    filaPivote = np.argmin(restrictions)
    return 0


def simplex(objective,restrictions,variables,maximize):
    cPivot = columnaPivote(objective)
    print(cPivot)
    var = np.array([('x1',3.0),('x2',2.8),('s2',1.2)])
    value = 370.0
    tuplaSolucion = (var, value)
    return tuplaSolucion



objective = np.array([30.0, 100.0, 0, 0, 0, -100000.0])
restrictions = np.matrix('1 1 1 0 0 0 7.0; 4.0,10.0,0,1,0,0,40.0;10.0 0 0 0 -1 1 30.0')
variables = np.array(['x1', 'x2', 's1', 's2', 's3', 'a3'])
maximize = "true"
ecuacion = "-3.8x1 + 5x2 - 2x3"
restriccion = "-3.8x1 + 5x2 -2x3 <= 35"
print(parse_equation(ecuacion))
print(parse_restriction(restriccion))
np.set_printoptions(suppress=True)
print(simplex(objective,restrictions,variables,maximize))