def fractionalKnapsack(n,k,v,w):
    value = 0.0
    ratio = {}
    for i in range(n):
        ratio[v[i]/w[i]] = [v[i],w[i]]
    for i in sorted(ratio.keys(),reverse = True):
        vw = ratio[i]
        if k == 0:
            return value
        a = min(vw[1],k)
        value += a*i
        k -= a
        ratio[i][1] -= a
    return value
N,K = map(int,input().split())
V = []
W = []
for i in range(N):
    x,y = map(int,input().split())
    V.append(x)
    W.append(y)
print(fractionalKnapsack(N,K,V,W))