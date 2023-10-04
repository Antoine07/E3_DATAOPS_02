"""
Ecrire une fonction qui permet de vérifier qu'une liste de caractères ne contient que des majuscules.

"""

def testUpper(l):
    # On vérifie une condition 
    assert len(l) > 0 

    for e in l:
        if e != e.upper() :
            return False

    return True
# testUpper([])
try:
    # un ternaire
    print("Valid") if testUpper([]) else print("invalid")
except AssertionError:
    print("La liste est vide")