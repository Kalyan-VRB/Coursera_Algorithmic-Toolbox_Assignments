def binarySearch(array, low, high, search, output):
    mid = low + (high - low) // 2
    if low > high:
        return output
    elif array[mid] == search:
        output.append(mid)
        return binarySearch(array, low, mid - 1, search, output)
    elif search > array[mid]:
        return binarySearch(array, mid + 1, high, search, output)
    else:
        return binarySearch(array, low, mid - 1, search, output)


n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
for i in range(m):
    output = binarySearch(arr1, 0, n - 1, arr2[i], [])
    if len(output) == 0:
        print(-1, end=" ")
    else:
        print(output[-1], end=" ")
