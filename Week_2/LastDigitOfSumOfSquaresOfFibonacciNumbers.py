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
    M = N + 1
    F = [0,1]
    P = pisanoPeriod(10)
    M = M % P
    N = N % P
    P = max(M,N)
    for i in range(2,P + 1):
        F.append(F[i-1]+F[i-2])
    digit1 = F[N] % 10
    digit2 = F[M] % 10
    print((digit1*digit2)%10)


