import csv
import os
file_path = 'notes.csv'
# chemin absolu
path = os.path.abspath(file_path)

stream = open('notes.csv', 'r',  newline='')

reader = csv.reader(stream, delimiter = ',')

# print(reader)

count, coeff, s = 0, 0, 0

for line in reader:
    # print(line)
    if count == 0:
        count += 1
        continue

    n, c = float(line[0]), float(line[1])
    s += n*c 
    coeff += c
    count += 1


print(f"Moyenne : {round(s/coeff, 1)}")

