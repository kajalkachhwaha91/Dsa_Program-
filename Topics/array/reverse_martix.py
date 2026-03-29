n = int(input())

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 1: Transpose
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Step 2: Reverse each row
for i in range(n):
    matrix[i].reverse()

# Print result
for row in matrix:
    print(*row)