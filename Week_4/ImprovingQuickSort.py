import random


def partition(arr, low, high):
    x = arr[low]
    m1 = low
    for i in range(low + 1, high + 1):
        if arr[i] < x:
            m1 += 1
            arr[m1], arr[i] = arr[i], arr[m1]
    arr[m1], arr[low] = arr[low], arr[m1]
    m2 = m1
    x = arr[m1]
    for i in range(m1 + 1, high + 1):
        if arr[i] == x:
            m2 += 1
            arr[m2], arr[i] = arr[i], arr[m2]
    arr[m2], arr[m1] = arr[m1], arr[m2]
    return m1, m2


def quickSort(arr, low, high):
    if low >= high:
        return
    # k = random.randint(low, high)
    # arr[k], arr[low] = arr[low], arr[k]
    m1, m2 = partition(arr, low, high)
    quickSort(arr, low, m1 - 1)
    quickSort(arr, m2 + 1, high)


n = int(input())
arr = list(map(int, input().split()))
quickSort(arr, 0, n - 1)
for i in arr:
    print(i, end=" ")
