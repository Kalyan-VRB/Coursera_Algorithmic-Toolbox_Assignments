def minPoints(n,p):
    points = []
    endPoint = p[0][1]
    points.append(str(p[0][1]))
    i = 1
    while i < n:
        if p[i][0] > endPoint:
            endPoint = p[i][1]
            points.append(str(endPoint))
        i += 1
    return points
N = int(input())
P = []
for i in range(N):
    x,y = map(int,input().split())
    P.append([x,y])
picked = minPoints(N,sorted(P,key = lambda x: x[1]))
print(len(picked))
print(" ".join(picked))