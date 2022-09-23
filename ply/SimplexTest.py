import numpy as np

import Lexer


# Se crea una tabla vacia, con suficientes filas y columnas para abarcar las variables y restricciones
def generateMatrix(variables, constraints):
    table = np.zeros((constraints + 1, variables + constraints + 2))
    return table

def parseEquation(equation):
    thisEquation = Lexer.plyParse(equation)
    dictionary = {}

    for item in thisEquation.dictionary:
        dictionary[item.variable.replace('+', '')] = item.coeff
    return dictionary

def parseRestriction(restriction):
    restDictionary = {}
    greaterBound = False

    thisRest = Lexer.plyParse(restriction)

    for rest in thisRest.dictionary:
        restDictionary[rest.variable] = rest.coeff

    if (thisRest.restriction.type == "<="):
        greaterBound = True
    return restDictionary, thisRest.restriction.value, greaterBound

def parseProblem(objective, restrictions, maximize):
    parsedObjective = parseEquation(objective)
    matrix = generateMatrix(len(parsedObjective), len(restrictions))
    generateConstraints(matrix, restrictions)
    generateObjectiveFunction(matrix, parsedObjective)

    simplex(matrix, maximize)

def simplex(matrix, boolMaximize):
    if boolMaximize == True:
        print(maximize(matrix))
    else:
        print(minimize(matrix))

def simplex_solver(objective, restrictions, maximize):
    parseProblem(objective, restrictions, maximize)










def obtainRestrictions(matrix, equation):
    restrictionDictionaries = []
    values = []
    greaterBounds = []

    for index in range(0, len(equation)):
        temp1, temp2, temp3 = parseRestriction(equation[index])

        restrictionDictionaries.insert(index, temp1)
        values.insert(index, temp2)
        greaterBounds.insert(index, temp3)

    rows = len(equation)
    cols = len(matrix[0, :]) - len(equation) - 1
    restrictions = np.zeros((int(rows), int(cols)))

    for index in range(0, len(equation)):
        j = 0

        for j in range(0, len(restrictionDictionaries[index])):
            tempDict = restrictionDictionaries[index]

            if (greaterBounds[index] == True):
                restrictions[index][j] = (float(tempDict["x{}".format(j + 1)]))
            else:
                restrictions[index][j] = (float(tempDict["x{}".format(j + 1)]) * -1)

        if (greaterBounds[index] == True):
            restrictions[index][cols - 1] = float(values[index])
        else:
            restrictions[index][cols - 1] = float(values[index]) * -1

    return restrictions




# Revisan si se van a necesitar varios pivotes
def nextRound_columns(table):
    minimum = min(table[:-1, -1])
    if minimum >= 0:
        return False
    else:
        return True


def nextRound_rows(table):
    lr = len(table[:, 0])
    minimum = min(table[lr - 1, :-1])
    if minimum >= 0:
        return False
    else:
        return True


def findNegatives_columns(table):
    lc = len(table[0, :])
    minimum = min(table[:-1, lc - 1])

    if minimum == -0.0000000:
        minimum = 0

    if minimum <= 0:
        index = np.where(table[:-1, lc - 1] == minimum)[0][0]
    else:
        index = None
    return index


def findNegatives_rows(table):
    lr = len(table[:, 0])
    minimum = min(table[lr - 1, :-1])

    if minimum <= 0:
        index = np.where(table[lr - 1, :-1] == minimum)[0][0]
    else:
        index = None
    return index


def locatePivot(table):
    total = []
    r = findNegatives_columns(table)
    row = table[r, :-1]
    minimum = min(row)
    c = np.where(row == minimum)[0][0]
    col = table[:-1, c]

    for i, b in zip(col, table[:-1, -1]):
        if i ** 2 > 0 and b / i > 0:
            total.append(b / i)
        else:
            total.append(50000)
    index = total.index(min(total))
    return [index, c]


def locatePivot_bottomRow(table):
    if nextRound_rows(table):
        total = []
        r = findNegatives_rows(table)

        for i, b in zip(table[:-1, r], table[:-1, -1]):
            if b / i > 0 and i ** 2 > 0:
                total.append(b / i)
            else:
                total.append(10000)
        index = total.index(min(total))
        return [index, r]


def pivot(row, col, table):
    length_rows = len(table[:, 0])
    length_cols = len(table[0, :])
    tempTable = np.zeros((length_rows, length_cols))
    pr = table[row, :]


    if table[row, col] ** 2 > 0:
        e = 1 / table[row, col]
        r = pr * e

        for item in r:
            if (item == -0.0):
                item = 0.0

        for i in range(len(table[:, col])):
            k = table[i, :]
            c = table[i, col]
            if list(k) == list(pr):
                continue
            else:
                tempTable[i, :] = list(k - r * c)
        tempTable[row, :] = list(r)
        return tempTable
    else:
        print('Cannot pivot on this element.')


def convert(equation):
    equation = equation.split(',')
    if 'G' in equation:
        g = equation.index('G')
        del equation[g]
        equation = [float(i) * -1 for i in equation]
        return equation
    if 'L' in equation:
        l = equation.index('L')
        del equation[l]
        equation = [float(i) for i in equation]
        return equation


def convert_minimization(table):
    table[-1, :-2] = [-1 * i for i in table[-1, :-2]]
    table[-1, -1] = -1 * table[-1, -1]
    return table


def generateVariables(table):
    lengthCols = len(table[0, :])
    lengthRows = len(table[:, 0])
    var = lengthCols - lengthRows - 1
    varTable = []
    for i in range(var):
        varTable.append('x' + str(i + 1))
    return varTable


# Verifica si es posible agregar mas de una restriccion a la tabla, revisando
# si hay espacio disponible
def addConstraints(table):
    lengthRows = len(table[:, 0])
    empty = []

    for i in range(lengthRows):
        total = 0

        for j in table[i, :]:
            total += j ** 2
        if total == 0:
            empty.append(total)
    if len(empty) > 1:
        return True
    else:
        return False


# Utilizando la Tabla y la Ecuacion, se definen todas las restricciones y se crea una tabla
# Del tamano apropiado
def generateConstraints(table, equation):
    if addConstraints(table) == True:
        lengthCols = len(table[0, :])
        lengthRows = len(table[:, 0])
        var = lengthCols - lengthRows - 1
        j = 0
        colCounter = 0
        equation = obtainRestrictions(table, equation)

        for i in range (0, len(equation[:, 0])):
            while j < lengthRows:
                row_check = table[i, :]
                total = 0

                for j in row_check:
                    total += float(j ** 2)
                if total == 0:
                    row = row_check
                    break
                j += 1
            j = 0

            while j < len(equation[i]) - 1:
                row[j] = equation[i][j]
                j += 1
            row[-1] = equation[i][-1]
            row[var + colCounter] = 1
            colCounter += 1
    else:
        print('Cannot add another constraint.')


# Verifica si es posible agregar la funcion objetivo
def addObjectiveFunction(table):
    lengthRows = len(table[:, 0])
    empty = []

    for i in range(lengthRows):
        total = 0
        for j in table[i, :]:
            total += j ** 2
        if total == 0:
            empty.append(total)
    if len(empty) == 1:
        return True
    else:
        return False


def generateObjectiveFunction(table, equation):
    if addObjectiveFunction(table) == True:
        equationArray = []

        for item in equation.keys():
            equationArray.append(float(equation[item]))
        equationArray.append(0.0)

        lr = len(table[:, 0])
        row = table[lr - 1, :]
        i = 0

        while i < len(equationArray) - 1:
            row[i] = equationArray[i] * -1
            i += 1
        row[-2] = 1
        row[-1] = equationArray[-1]
    else:
        print('You must finish adding constraints before the objective function can be added.')


def maximize(table):
    while nextRound_columns(table) == True:
        table = pivot(locatePivot(table)[0], locatePivot(table)[1], table)
    while nextRound_rows(table) == True:
        table = pivot(locatePivot_bottomRow(table)[0], locatePivot_bottomRow(table)[1], table)

    lengthColumns = len(table[0, :])
    lengthRows = len(table[:, 0])
    var = lengthColumns - lengthRows - 1
    i = 0
    val = {}

    for i in range(var):
        column = table[:, i]
        columnSum = sum(column)
        maximum = max(column)

        if float(columnSum) == float(maximum):
            loc = np.where(column == maximum)[0][0]
            val[generateVariables(table)[i]] = table[loc, -1]
        else:
            val[generateVariables(table)[i]] = 0
    val['max'] = table[-1, -1]
    return val


def minimize(table):
    table = convert_minimization(table)
    while nextRound_columns(table) == True:
        table = pivot(locatePivot(table)[0], locatePivot(table)[1], table)
    while nextRound_rows(table) == True:
        table = pivot(locatePivot_bottomRow(table)[0], locatePivot_bottomRow(table)[1], table)

    lengthCols = len(table[0, :])
    lengthRows = len(table[:, 0])
    var = lengthCols - lengthRows - 1
    i = 0
    val = {}

    for i in range(var):
        column = table[:, i]
        columnSum = sum(column)
        maximum = max(column)

        if float(columnSum) == float(maximum):
            loc = np.where(column == maximum)[0][0]
            val[generateVariables(table)[i]] = table[loc, -1]
        else:
            val[generateVariables(table)[i]] = 0
    val['min'] = table[-1, -1] * -1
    return val





simplex_solver("0.65x1 + 0.45x2", ["2x1 + 3x2 <= 400", "3x1 + 1.5x2 <= 300", "x1 <= 90"], True)
simplex_solver("30x1 + 100x2", ["x1 + x2 <= 7", "4x1 + 10x2 <= 40", "10x1 >= 30"], True)
simplex_solver("3x1 + 8x2", ["x1 + 4x2 >= 3.5" , "x1 + 2x2 >= 2.5"], False)
