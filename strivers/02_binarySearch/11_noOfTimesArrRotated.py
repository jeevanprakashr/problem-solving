def findKRotations(arr):
    # should find minimum in the arr using 09_findMinInRotatedArr and return its index
    # Eg: [3, 4, 5, 1, 2]    ans = 3 (3 times rotated)
    n = len(arr)
    low = 0
    high = n - 1
    ans = float("inf")
    index = -1
    while low <= high:
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            break
        mid = low + ((high - low) // 2)
        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            low = mid + 1
        else:
            if arr[mid] < ans:
                ans = arr[mid]
                index = mid
            high = mid - 1
    return index

arr = [3, 4, 5, 1, 2]
print(findKRotations(arr))
# for duplicates - 08