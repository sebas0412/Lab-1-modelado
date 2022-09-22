import numpy as np


# Se crea una tabla vacia, con suficientes filas y columnas para abarcar las variables y restricciones
def generateMatrix(variables, constraints):
    table = np.zeros((constraints + 1, variables + constraints + 2))
    return table


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


def locatePivot_rows(table):
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
            total.append(10000)
    index = total.index(min(total))
    return [index, c]


def locatePivot_columns(table):
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


#Utilizando la Tabla y la Ecuacion, se definen todas las restricciones y se crea una tabla
#Del tamano apropiado
def constrain(table, equation):
    if addConstraints(table) == True:
        lengthCols = len(table[0, :])
        lengthRows = len(table[:, 0])
        var = lengthCols - lengthRows - 1
        j = 0

        while j < lengthRows:
            row_check = table[j, :]
            total = 0

            for i in row_check:
                total += float(i ** 2)
            if total == 0:
                row = row_check
                break
            j += 1
        equation = convert(equation)
        i = 0

        while i < len(equation) - 1:
            row[i] = equation[i]
            i += 1
        row[-1] = equation[-1]
        row[var + j] = 1
    else:
        print('Cannot add another constraint.')


#Verifica si es posible agregar la funcion objetivo
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


def objective(table, equation):
    if addObjectiveFunction(table) == True:
        equation = [float(i) for i in equation.split(',')]
        lr = len(table[:, 0])
        row = table[lr - 1, :]
        i = 0

        while i < len(equation) - 1:
            row[i] = equation[i] * -1
            i += 1
        row[-2] = 1
        row[-1] = equation[-1]
    else:
        print('You must finish adding constraints before the objective function can be added.')


def maximize(table):
    while nextRound_columns(table) == True:
        table = pivot(locatePivot_rows(table)[0], locatePivot_rows(table)[1], table)
    while nextRound_rows(table) == True:
        table = pivot(locatePivot_columns(table)[0], locatePivot_columns(table)[1], table)

    lengthColumns = len(table[0, :])
    lengthRows = len(table[:, 0])
    var = lengthColumns - lengthRows - 1
    i = 0
    val = {}

    for i in range(var):
        column = table[:, i]
        colSum = sum(column)
        maximum = max(column)

        if float(colSum) == float(maximum):
            loc = np.where(column == maximum)[0][0]
            val[generateVariables(table)[i]] = table[loc, -1]
        else:
            val[generateVariables(table)[i]] = 0
    val['max'] = table[-1, -1]
    return val

def minimize(table):
    table = convert_minimization(table)
    while nextRound_columns(table) == True:
        table = pivot(locatePivot_rows(table)[0], locatePivot_rows(table)[1], table)
    while nextRound_rows(table) == True:
        table = pivot(locatePivot_columns(table)[0], locatePivot_columns(table)[1], table)

    lengthCols = len(table[0, :])
    lengthRows = len(table[:, 0])
    var = lengthCols - lengthRows - 1
    i = 0
    val = {}

    for i in range(var):
        column = table[:, i]
        colSums = sum(column)
        maximum = max(column)

        if float(colSums) == float(maximum):
            loc = np.where(column == maximum)[0][0]
            val[generateVariables(table)[i]] = table[loc, -1]
        else:
            val[generateVariables(table)[i]] = 0
            val['min'] = table[-1, -1] * -1
    return val


matrix = generateMatrix(2, 3)

constrain(matrix, '1,1,L,7')
constrain(matrix, '4,10,L,40')
constrain(matrix, '10,0,G,30')

objective(matrix, '30,100,0')
print(maximize(matrix))