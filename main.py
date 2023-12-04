from math import sqrt

from z3.z3 import *

def increment_elements(lst):
    # Créer un contexte Z3
    ctx = Context()

    # Déclarer des variables Z3 pour chaque élément de la liste
    z3_list = [Int(f'x{i}', ctx=ctx) for i in range(len(lst))]
    print(z3_list)

    # Créer un solveur
    solver = Solver(ctx=ctx)

    # Ajouter l'invariant initial (tous les éléments sont positifs)
    for x in lst:
        if x > 0:
            solver.add(True)
        else:
            solver.add(False)
            pass


    # Appliquer l'algorithme (incrémenter chaque élément de 1)
    for i in range(len(lst)):
        solver.add(z3_list[i] == lst[i] - 1)

    # Ajouter l'invariant final (tous les éléments sont positifs)
    final_positivity = And([x >= 0 for x in z3_list])
    print(final_positivity)
    solver.add(final_positivity)


    # Vérifier si toutes les contraintes sont satisfaisables
    if solver.check() == sat:
        print("L'algorithme maintient l'invariant.")
        # Afficher la solution si elle est satisfaisable
        model = solver.model()
        final_list = [model[x].as_long() for x in z3_list]
        print("Liste finale:", final_list)
    else:
        print("L'algorithme ne maintient pas l'invariant.")

# Testons l'algorithme avec une liste d'exemple
example_list = [1, 3, 4]
increment_elements(example_list)


def algorithme():
    x = int(input("Donnez une valeur à X"))
    y = int(input("Donnez une valeur à Y"))
    if x > y:
        y = y * 2
        x = x * 2
        if y < x:
            x = y - 10
            y = x - 10
            if x > 0 and y > 0:
                resultat = sqrt(x) + sqrt(y)
            else:
                resultat = x ** 2 + y ** 2
        else:
            resultat = x - y
    else:
        resultat = x + y
    return resultat
