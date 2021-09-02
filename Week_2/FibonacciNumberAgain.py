def pisanoPeriod(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1
N,M = map(int,input().split())
if N <= 1:
    print(N)
else:
    F = [0, 1]
    N=N%pisanoPeriod(M)
    for i in range(2,N+1):
        F.append(F[i-1]+F[i-2])
    print(F[N]%M)


