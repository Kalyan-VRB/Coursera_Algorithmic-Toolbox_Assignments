def mergeElements(arr, low, mid, high):
    n = mid - low + 1
    m = high - mid
    left = []
    right = []
    for i in range(n):
        left.append(arr[low + i])
    for i in range(m):
        right.append(arr[mid + i + 1])
    a = 0
    b = 0
    k = low
    while a < n and b < m:
        if left[a] <= right[b]:
            arr[k] = left[a]
            a += 1
        else:
            arr[k] = right[b]
            b += 1
        k += 1
    while a < n:
        arr[k] = left[a]
        a += 1
        k += 1
    while b < m:
        arr[k] = right[b]
        b += 1
        k += 1


def partition(arr, low, high):
    if low < high:
        mid = low + (high - low) // 2
        partition(arr, low, mid)
        partition(arr, mid + 1, high)
        mergeElements(arr, low, mid, high)


def majorityElement(n, arr):
    for i in range((n // 2) + n % 2):
        if arr[i] == arr[i + n // 2]:
            return 1
    return 0


n = int(input())
arr = list(map(int, input().split()))
partition(arr, 0, n - 1)
print(majorityElement(n, arr))
