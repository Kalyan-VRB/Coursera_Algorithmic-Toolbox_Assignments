def maxPairwiseProduct(arr,n):
    first_max_index = -1
    for i in range(n):
        if first_max_index == -1 or arr[first_max_index]<arr[i]:
            first_max_index = i
    second_max_index = -1
    for i in range(n):
        if i!=first_max_index and (second_max_index == -1 or arr[second_max_index]<arr[i]):
            second_max_index = i
    return arr[first_max_index]*arr[second_max_index]
N=int(input())
sequence=[int(a) for a in input().split()]
print(maxPairwiseProduct(sequence,N))
