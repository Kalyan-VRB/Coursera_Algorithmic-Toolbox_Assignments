def minNumDenom(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 5 or n == 10:
        return 1
    else:
        return n // 10 + (n % 10) // 5 + n % 5
n = int(input())
print(minNumDenom(n))