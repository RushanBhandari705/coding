# Transpose
A = [[9, 8, 7],
     [6, 5, 6]]

transpose = []

for i in range(len(A[0])):
    row = []
    for j in range(len(A)):
        row.append(A[j][i])
    transpose.append(row)

print("Transpose of Matrix A =")
for row in transpose:
    print(row)
