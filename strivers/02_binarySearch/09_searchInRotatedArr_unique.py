# sorted array of unique elements
# array rotated once
def searchInRotatedArr(arr, target):
    # Intuition:
    # Once checked for mid, find the sorted half of the array first and eliminate the correct half
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            # left half is sorted
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # right half is sorted
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
target = 1
print(searchInRotatedArr(arr, target))