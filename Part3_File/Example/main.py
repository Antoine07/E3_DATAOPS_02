import os
file_path = 'data.txt'
path = os.path.abspath(file_path)
# print(path)
stream = open(path, 'r')

# print(stream)

ligne = stream.readline()

while ligne != "":
    ligne = stream.readline()
    print(ligne)

stream.close()

print("--------------")

stream = open(path, 'r')
content = stream.readlines()
print(content)

stream.close()