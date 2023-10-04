# Les fichiers

## Ouverture du fichier

**path** est le **chemin absolu** dénotant le fichier à ouvrir (e.g. ''~/python/animals.txt')
r est le mode d'ouverture du fichier, ici en lecture seule

```python
stream = open(path, 'r')

# Fermeture du fichier
stream.close()
```

- Calculer le chemin absolu 

```python
import os
file_path = 'data.txt'
path = os.path.abspath(file_path)
# print(path)
stream = open(path, 'r')
# print(stream)

ligne = stream.readline()
while ligne != "":
    print(ligne)
    ligne = stream.readline()

stream.close()
```

## Lecture d'un fichier csv 

```python
import csv

stream = open('notes.csv', newline='')
reader = csv.reader(stream)

lines = []
for line in reader:
    lines.append(line)
print(lines)

```

## 01 Exercice moyenne

Faire la moyenne des notes du fichier notes.csv

## 02 Exercice encore sur les moyennes

1. Créez votre propre fichier de notes et faites la moyenne

2. ajouter des coefficents à vos notes et refaire la moyenne.
