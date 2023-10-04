"""
Créez une fonction qui calcule le prix TTC d'un prix HT

"""

def ttc(t, p):

    return round( (t + 1 ) * p , 2 )

print( ttc( 0.2, 1314.989 ))