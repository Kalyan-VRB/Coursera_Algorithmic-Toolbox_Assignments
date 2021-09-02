def pisanoPeriod(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1
N = int(input())
if N <= 1:
    print(N)
else:
    F = [0,1]
    M = pisanoPeriod(10)
    for i in range(2,M + 1):
        F.append(F[i-1]+F[i-2])
    digit = ((N // M) * sum(F) + sum(F[:1+N%M]))%10
    print(digit)


