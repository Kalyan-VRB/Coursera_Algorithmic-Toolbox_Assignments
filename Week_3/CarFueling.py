def minNumRefills(d,m,n,s):
    refills = 0
    currRefill = 0
    s = [0] + s + [d]
    while currRefill <= n:
        lastRefill = currRefill
        while currRefill <= n and s[currRefill+1] - s[lastRefill] <= m:
            currRefill = currRefill + 1
        if currRefill == lastRefill:
            return -1
        if currRefill <= n:
            refills += 1
    return refills
D = int(input())
M = int(input())
N = int(input())
S = list(map(int,input().split()))
print(minNumRefills(D,M,N,S))