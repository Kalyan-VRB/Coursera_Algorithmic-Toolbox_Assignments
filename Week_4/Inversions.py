def mergeElements(arr, low, mid, high,count):
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
            count+=1
        k += 1
    while a < n:
        arr[k] = left[a]
        a += 1
        k += 1
    while b < m:
        arr[k] = right[b]
        b += 1
        k += 1
    return count


def partition(arr, low, high,count):
    if low < high:
        mid = low + (high - low) // 2
        partition(arr, low, mid,count)
        partition(arr, mid + 1, high,count)
        count+=mergeElements(arr, low, mid, high,count)
    return count

n = int(input())
arr = list(map(int,input().split()))
print(partition(arr,0,n-1,0))