import numpy as np

def simplex(objective,restrictions,variables,maximize):
    tuplaSolucion = (objective,restrictions,variables,maximize)
    return tuplaSolucion

objective = np.array([30.0, 100.0, 0, 0, 0, -100000.0])
restrictions = np.matrix('1 1 1 0 0 0 7.0; 4.0,10.0,0,1,0,0,40.0;10.0 0 0 0 -1 1 30.0')
variables = np.array(['x1', 'x2', 's1', 's2', 's3', 'a3'])
maximize = "true"
np.set_printoptions(suppress=True)
print(simplex(objective,restrictions,variables,maximize))