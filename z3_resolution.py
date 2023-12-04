from z3.z3 import *

def detection_code_mort1():
    x = Int('x')
    x_0 = Int('x_0')
    y = Int('y')
    y_0 = Int('y_0')

    # Créer des solveur pour chaque cas de test solveur Z3

    solver_cas1 = Solver()


    # création condition pour le solver du cas de test 1 x > y & y > x
    condition_1_1 = x > y
    x_0 = x*2
    y_0 = y*2
    condition_1_2 = y_0 > x_0
    solver_cas1.add(condition_1_1,condition_1_2)

    if solver_cas1.check() == sat:
        print("ce code est atteignable avec " + solver_cas1.solver)
    else:
        print("ce code est inateignable, c'est un code mort")




def detection_code_mort2():
    x = Int('x')
    y = Int('y')

    # Créer des solveur pour chaque cas de test solveur Z3
    solver_cas2 = Solver()


    # création condition pour le solver du cas de test 2 x < y
    condition_2_1 = x > y
    solver_cas2.add(condition_2_1)

    if solver_cas2.check() == sat:
        print(f"ce code est atteignable avec {solver_cas2.model()}")
    else:
        print("ce code est inateignable, c'est un code mort")


def detection_code_mort3():
    x = Int('x')
    x_0 = Int('x_0')
    x_1 = Int('x_1')
    y = Int('y')
    y_0 = Int('y_0')
    y_1 = Int('y_1')

    # Créer des solveur pour chaque cas de test solveur Z3
    solver_cas3 = Solver()

    # création condition pour le solver du cas de test 3 x > y ,  y < x ,   x<0, y<0
    condition_3_1 = x > y
    x_0 = x * 2
    y_0 = y * 2
    condition_3_2 = y_0 < x_0
    x_1 = x_0 - 10
    y_1 = y_0 - 10
    condition_3_3 = And(x_1 < 0,y_1 < 0)
    solver_cas3.add(condition_3_1, condition_3_3, condition_3_2)

    if solver_cas3.check() == sat:
        print(f"ce code est atteignable avec {solver_cas3.model()}")
    else:
        print("ce code est inateignable, c'est un code mort")

def detection_code_mort4():
    x = Int('x')
    x_0 = Int('x_0')
    x_1 = Int('x_1')
    y = Int('y')
    y_0 = Int('y_0')
    y_1 = Int('y_1')

    # Créer des solveur pour chaque cas de test solveur Z3
    solver_cas4 = Solver()

    # création condition pour le solver du cas de test 3 x > y ,  y < x ,   x>0, y>0
    condition_4_1 = x > y
    x_0 = x * 2
    y_0 = y * 2
    condition_4_2 = y_0 < x_0
    x_1 = x_0 - 10
    y_1 = y_0 - 10
    condition_4_3 = And(x_1 > 0,y_1 > 0)
    solver_cas4.add(condition_4_1, condition_4_3, condition_4_2)

    if solver_cas4.check() == sat:
        print(f"ce code est atteignable avec {solver_cas4.model()}")
    else:
        print("ce code est inateignable, c'est un code mort")
'''
print("pour le cas de test 1 on a:")
detection_code_mort1()
print("pour le cas de test 2 on a:")
detection_code_mort2()
print("pour le cas de test 3 on a:")
detection_code_mort3()
print("pour le cas de test 4 on a:")
detection_code_mort4()
'''



def generation_cas_de_test4_2():
    x = Int('x')
    x_0 = Int('x_0')
    x_1 = Int('x_1')
    y = Int('y')
    y_0 = Int('y_0')
    y_1 = Int('y_1')

    # Créer des solveur pour chaque cas de test solveur Z3
    solver_cas4 = Solver()

    # création condition pour le solver du cas de test 3 x > y ,  y < x ,   x>0, y>0
    condition_4_1 = x > y
    x_0 = x * 2
    y_0 = y * 2
    condition_4_2 = y_0 < x_0
    x_1 = x_0 - 10
    y_1 = y_0 - 10
    #a revoir
    condition_4_3 = And(x_1 > 0,y_1 > 0,x_1+y_1==100)
    solver_cas4.add(condition_4_1, condition_4_3, condition_4_2)

    # Générer des cas de test
    test_cases = []

    while solver_cas4.check() == sat:
            model = solver_cas4.model()
            #print(model)
            test_case = (model[x].as_long(), model[y].as_long())
            test_cases.append(test_case)

            # Ajouter une contrainte pour éviter de générer le même cas de test
            solver_cas4.add(Or(x != model[x], y != model[y]))

    return test_cases

'''
test_cases = generation_cas_de_test4_2()
print("Cas de test générés :")
#print(test_cases)
for test_case in test_cases:
    print(f"x = {test_case[0]}, y = {test_case[1]}")

'''



#test D'invariant x>10 , y > 10


def detection_invariance_cas_de_test4_2():
    x = Int('x')
    x_0 = Int('x_0')
    x_1 = Int('x_1')
    y = Int('y')
    y_0 = Int('y_0')
    y_1 = Int('y_1')

    # Créer des solveur pour chaque cas de test solveur Z3
    solver_cas4 = Solver()

    # création condition pour le solver du cas de test 3 x > y ,  y < x ,   x>0, y>0
    condition_4_1 = x > y
    condition_4_1_1 = x > 10
    condition_4_1_2 = y > 10
    x_0 = x * 2
    y_0 = y * 2
    condition_4_2 = y_0 < x_0
    condition_4_2_1 = y_0 > 10
    condition_4_2_2 = x_0 > 10
    x_1 = x_0 - 10
    y_1 = y_0 - 10
    #a revoir
    condition_4_3 = And(x_1 > 0,y_1 > 0,y_0 > 10,x_0 > 10)
    solver_cas4.add(condition_4_1, condition_4_3, condition_4_2,condition_4_1_1,condition_4_2_1,condition_4_1_2,condition_4_2_2)

    if solver_cas4.check() == sat:
        print("invariant validé")
        print(solver_cas4.model())
    else:
        print("invariant non valide ")

detection_invariance_cas_de_test4_2()






