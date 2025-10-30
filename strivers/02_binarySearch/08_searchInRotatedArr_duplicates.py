# sorted array of unique elements
# array rotated once
def searchInRotatedArr(arr, target):
    '''
    07_searchInRotatedArr_unique can work but will fail in one edge case where
    arr[low] = arr[mid] = arr[high]
    like [3, 1, 2, 3, 3, 3, 3]
    when this occurs, try to shrink the search space until the case goes away
    '''
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == target:
            return mid
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            # shrink the search space
            low += 1
            high -= 1
            continue
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

arr = [3, 1, 2, 3, 3, 3, 3]
target = 1
print(searchInRotatedArr(arr, target))