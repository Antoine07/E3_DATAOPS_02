import csv
import os
file_path = 'notes.csv'
# chemin absolu
path = os.path.abspath(file_path)

stream = open('notes.csv', 'r',  newline='')

reader = csv.reader(stream, delimiter = ';')

# print( list( reader) ) 
count = 0
s = 0
for line in reader:
    # print(line)
    for n in line:
        count += 1
        s += float( n )

print( f"La moyenne : { round(s/count , 2) }" )


