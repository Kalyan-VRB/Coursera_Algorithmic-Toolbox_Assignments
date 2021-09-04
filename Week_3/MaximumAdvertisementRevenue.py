def maxDotProduct(n,a,b):
    product = 0
    a.sort()
    b.sort()
    for i in range(n):
        product += a[i]*b[i]
    return product
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(maxDotProduct(N,A,B))