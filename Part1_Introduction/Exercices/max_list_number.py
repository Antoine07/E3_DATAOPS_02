"""
Ecrire une fonction qui permet de retourner le maximun d'une liste de nombres avec son indice. Vous devez utiliser uniquement les deux fonction **builtins** suivantes de Python : len et index.

Vous pouvez vérifiez la cohérence de votre programme en vérifiant le type et que la liste n'est pas vide.

"""

import random
m = []
N = 20
Alea = 100 
Noise = 1_000
for _ in range(1, N):
    n = random.randint(1, Noise )
    m.append( random.randint(1, n ) )

print(m)

elMax = m[0]
for i in range(1, len(m)):
    if m[i] > elMax:
        elMax = m[i]


print(elMax)