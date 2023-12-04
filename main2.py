from z3.z3 import *

def verif_algo():
    # Créer un contexte Z3

    # Déclarer des variables Z3 pour chaque élément de la liste
    x = Int('x')
    y = Int('y')

    # Créer un solveur
    solver = Solver()

    # Ajouter l'invariant initial (tous les éléments sont positifs)
    solver.add(x<5 , y < 5)


    solver.add(x+y>10)





    # Vérifier si toutes les contraintes sont satisfaisables
    if solver.check() == sat:
        print("L'algorithme est correct")
        # Afficher la solution si elle est satisfaisable
        model = solver.model()
        print(model)
    else:
        print("code mort")

# Testons l'algorithme avec une liste d'exemple

verif_algo()
