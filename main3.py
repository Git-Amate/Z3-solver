from z3.z3 import *


def solve_quadratic_equation(a, b, c):
    # Variables
    x = Real('x')

    # Créer un solveur Z3
    solver = Solver()

    # Ajouter les contraintes de l'équation quadratique
    equation = a * x**2 + b * x + c == 0
    solver.add(equation)

    # Vérifier la satisfaisabilité
    result = solver.check()

    if result == sat:
        print(f"Les solutions réelles de l'équation sont : {solver.model()}")
    else:
        print("L'équation n'a pas de solution réelle.")

# Exemple d'utilisation
solve_quadratic_equation(1, -3, 2)
solve_quadratic_equation(1, 2, 1)
solve_quadratic_equation(1, 0, -1)

