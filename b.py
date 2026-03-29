# Matrix Multiplication
A = [[1, 2],
     [2, 4]]

B = [[9, 8],
     [8, 8]]

# Result matrix initialization
result = [[0, 0],
          [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Matrix A x B =")
for row in result:
    print(row)
