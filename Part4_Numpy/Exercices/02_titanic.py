import numpy as np
import urllib.request

"""

1. Donnez le nombre de femmes qui ont survécu.

"""

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = urllib.request.urlopen(url)

print(data)

titanic_data = np.genfromtxt(data, delimiter=',', dtype=str, skip_header=1)

# # Afficher les premières lignes pour vérifier le chargement
print(titanic_data[:5])


