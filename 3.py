#WAP that opens file.txt in r+ mode, reads the content, and then overwrites the beginning with "Start".
with open('file.txt', 'r+') as file:
    file.write("\nStart")

with open('file.txt') as file:
    print(file.read())