def isGreaterOrEqual(x,y):
    if x+y >= y+x:
        return True
    return False

def maximumSalary(digits):
    salary = ""
    while len(digits)!= 0:
        maxDigit = -1
        for i in digits:
            if isGreaterOrEqual(str(i),str(maxDigit)):
                maxDigit = i
        salary += str(maxDigit)
        digits.remove(maxDigit)
    return salary
N = int(input())
Digits = list(map(int,input().split()))
print(maximumSalary(Digits))