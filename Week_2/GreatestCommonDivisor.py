def gcd(M,N):
    if N == 0:
        return M
    else:
        return gcd(N,M % N)
m,n = map(int,input().split())
if m>n:
    print(gcd(m,n))
else:
    print(gcd(n,m))