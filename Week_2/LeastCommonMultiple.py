def gcd(M,N):
    if N == 0:
        return M
    else:
        return gcd(N,M % N)
def lcm(M,N):
    return (M//gcd(M,N))*N
m, n = map(int, input().split())
if m > n:
    print(lcm(m, n))
else:
    print(lcm(n, m))