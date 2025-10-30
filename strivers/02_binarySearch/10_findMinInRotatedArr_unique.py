def findMinInRotatedArr(arr):
    # Intutition:
    # 1. Find the sorted half
    # 2. Take the min of sorted half and eliminate it
    # 3. Move to the unsorted half and repeat while updated actual result with the min
    n = len(arr)
    low = 0
    high = n - 1
    ans = float("inf")
    while low <= high:
        if arr[low] <= arr[high]:
            # search space is already sorted, then always arr[low] will be smaller in that search space
            ans = min(ans, arr[low])
            break
        mid = low + ((high - low) // 2)
        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid + 1
        else:
            ans = min(ans, arr[mid])
            high = mid - 1
    return ans

arr = [4, 5, 6, 7, 0, 1, 2]
arr = [7, 8, 1, 2, 3, 4, 5, 6]
arr = [4, 5, 1, 2, 3]
print(findMinInRotatedArr(arr))

# duplicates can be done using same method used in 08_searchInRotatedArr_duplicates
        