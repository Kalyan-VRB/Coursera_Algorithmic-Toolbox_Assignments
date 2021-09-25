def maximumWeight(capacity, n, weights):
    value = [[0] * (n + 1) for i in range(capacity + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            value[j][i] = value[j][i - 1]
            if weights[i] <= j:
                v = value[j - weights[i]][i - 1] + weights[i]
                if value[j][i] < v:
                    value[j][i] = v
    return value[capacity][n]


W, N = map(int, input().split())
items = [0] + list(map(int, input().split()))
print(maximumWeight(W, N, items))
