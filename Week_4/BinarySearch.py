def binarySearch(array, low, high, search):
    mid = low + (high - low) // 2
    if low > high:
        return -1
    elif array[mid] == search:
        return mid
    elif search > array[mid]:
        return binarySearch(array, mid + 1, high, search)
    else:
        return binarySearch(array, low, mid - 1, search)

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
for i in range(m):
    print(binarySearch(arr1, 0, n-1, arr2[i]), end=" ")
