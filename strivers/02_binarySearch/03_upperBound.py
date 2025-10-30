# same as 02_lowerBound, but upper bound is index; arr[index] > x; x is target
def upperBound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [2, 3, 6, 7, 8, 8, 11, 11, 11, 12]
target = 10
print(upperBound(arr, target))