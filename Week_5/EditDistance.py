def editDistance(A, B):
    n = len(A) - 1
    m = len(B) - 1
    D = [[0] * m for i in range(n)]
    for i in range(n):
        D[i][0] = i
    for i in range(m):
        D[0][i] = i
    for j in range(1, m):
        for i in range(1, n):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            misMatch = D[i - 1][j - 1] + 1
            if A[i] == B[j]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, misMatch)
    return D[n - 1][m - 1]


string1 = input()
string2 = input()
print(editDistance('0' + string1 + '0', '0' + string2 + '0'))
