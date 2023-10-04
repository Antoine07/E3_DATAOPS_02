"""
En utilisant une boucle afficher la table 7

Puis créez une fonction pour afficher toutes les tables

""" 

for i in range(1, 11):
    print( i * 7 )

def mult(n):
    l = []
    for i in range(1, 11):
        # print( i * n )
        l.append( i * n )

    return l 

print( mult(7 ))
print( mult(8 ))
print( mult(2 ))
    