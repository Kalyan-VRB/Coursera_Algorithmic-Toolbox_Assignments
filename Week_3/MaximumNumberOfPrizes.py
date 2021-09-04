def findPrizes(n):
    if n == 1:
        return ["1"]
    prizes = []
    num = n
    for i in range(1,2+n//2):
        if 2*i < num:
            prizes.append(str(i))
            num -= i
        else:
            prizes.append(str(num))
            break
    return  prizes

N = int(input())
bestPrizes = findPrizes(N)
print(len(bestPrizes))
print(" ".join(bestPrizes))
