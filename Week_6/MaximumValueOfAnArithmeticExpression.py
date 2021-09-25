def minAndMax(i, j, Max, Min, operator):
    minValue = float('inf')
    maxValue = float('-inf')
    for k in range(i, j):
        a = int(eval(str(Max[i][k]) + operator[k] + str(Max[k + 1][j])))
        b = int(eval(str(Max[i][k]) + operator[k] + str(Min[k + 1][j])))
        c = int(eval(str(Min[i][k]) + operator[k] + str(Max[k + 1][j])))
        d = int(eval(str(Min[i][k]) + operator[k] + str(Min[k + 1][j])))
        minValue = min(minValue, a, b, c, d)
        maxValue = max(maxValue, a, b, c, d)
    return minValue, maxValue


def parentheses(d, op):
    n = len(digits)
    M = [[0] * n for _ in range(n)]
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1, n - 1):
        for i in range(1, n - s):
            j = i + s
            m[i][j], M[i][j] = minAndMax(i, j, M, m, op)
    return M[1][n - 1]


expression = input()
digits = [0]
operators = ['0']
for i in expression:
    if i.isdigit():
        digits.append(int(i))
    else:
        operators.append(i)
print(parentheses(digits, operators))
