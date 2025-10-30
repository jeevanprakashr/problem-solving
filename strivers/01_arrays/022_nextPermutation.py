def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def nextPermutation(arr):
    # Step 1: find the first drop point from the right
    #         reason: a decending order comb is the maximum and can't be rearranged to get next maximum
    # Step 1.1: if no drop point found, then it is the maximum comb,
    #           so reverse the arr to get the minimum comb which can be considered as the next permutation
    # Step 2: find the closest greater number to the right than the drop point number and swap them
    # Step 3: since the remaining elements to the right of the drop point is already in decending order, reverse them
    #         to get the smallest comb in the right
    n = len(arr)
    dropIdx = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            dropIdx = i
            break
    if dropIdx == -1:
        reverse(arr, 0 , n - 1)
        return arr
    for i in range(n - 1, dropIdx, -1):
        if arr[i] > arr[dropIdx]:
            arr[i], arr[dropIdx] = arr[dropIdx], arr[i]
            break
    reverse(arr, dropIdx + 1, n - 1)
    return arr

arr = [2, 1, 5, 4, 3, 0, 0]
arr = [5, 4, 3, 2, 1]
arr = [1, 2, 3, 4, 5]
nextPermutation(arr)
print(arr)
    