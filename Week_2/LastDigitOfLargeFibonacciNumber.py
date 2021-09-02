N = int(input())
if N <= 1:
    print(N)
else:
    a = 0
    b = 1
    for i in range(2,N + 1):
        b = a % 10 + b % 10
        a = b % 10 - a % 10
    print(b % 10)


