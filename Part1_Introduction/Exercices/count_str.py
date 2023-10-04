"""
1. Comptez le nombre de "i"

2. Comptez le nombre de chacune des lettres et mettre le résultat dans un dictionnaire.
""" 

m = "mississippi"

print( set(m) )

stat = {}
for letter in set(m) :
    stat[letter] = 0
    for e in m:
        if e == letter :
            stat[letter] += 1

print(stat)