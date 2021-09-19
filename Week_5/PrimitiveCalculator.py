N = int(input())
matrix = [0] * (N + 1)
for i in range(1, N + 1):
    matrix[i] = matrix[i - 1] + 1
    if i % 2 == 0:
        matrix[i] = min(1 + matrix[i // 2], matrix[i])
    if i % 3 == 0:
        matrix[i] = min(1 + matrix[i // 3], matrix[i])
print(matrix[N] - 1)
