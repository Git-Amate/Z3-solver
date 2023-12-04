from z3.z3 import *
from math import sqrt

def detection_code_mort():
    t = []
    x = Int('x')
    y = Int('y')

    # Créer un solveur Z3
    solver = Solver()

    #creation des conditions
    condition1 = (x%2!=0 , y>0)
    solver.add(condition1)
    somme = x + y
    condition2 = somme > 10
    condition3 = somme % 2 == 0
    solver.add(condition2)
    solver.add(condition3)
    result = solver.check()

    if result == sat:
        print("code atteignable")
        print(solver.model())
    else:
        print("code mort")

detection_code_mort()
