#WAP that opens a file named log.txt in append mode and adds the line "New entry added".

with open('log.txt', 'a') as file:
    file.write("\nNew entry added")

with open('log.txt') as file:
    print(file.read())
