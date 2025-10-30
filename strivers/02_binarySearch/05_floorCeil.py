# floor - largest number <= x
# ceil - smallest number >= x  (lower bound)
def floor(arr, x):
    n = len(arr)
    ans = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] <= x:
            ans = arr[mid]
            low = mid + 1  # we want largest, so move to the right
        else:
            high = mid - 1
    return ans

def ceil(arr, x):
    n = len(arr)
    ans = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] >= x:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [10, 20, 30, 40, 50]
x = 25
print([floor(arr, x), ceil(arr, x)])