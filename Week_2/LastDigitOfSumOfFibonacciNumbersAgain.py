def pisanoPeriod(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1
N,M = map(int,input().split())
F = [0,1]
P = pisanoPeriod(10)
for i in range(2,P + 1):
    F.append((F[i-1]+F[i-2])%10)
digit1 = ((M // P) * sum(F[:M]) + sum(F[:1+M%P]))%10
digit2 = ((N // P) * sum(F[:N]) + sum(F[:N%P]))%10
print((digit1-digit2)%10)


