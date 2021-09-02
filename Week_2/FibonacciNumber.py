N = int(input())
if N == 0:
    print('0')
elif N == 1:
    print('1')
elif N >= 1:
    F = [0, 1]
    for i in range(2,N+1):
        F.append(F[i-1]+F[i-2])
    print(F[N])


