# given a sorted array and a target find the lower bound of the target
# lower bound is the smallest index where arr[index] >= x ; x -> target
# this problem can be also asked as search insert point (04th problem); find the index where the given target would go in the array
def lowerBound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n     # hypothetical max answer when there is no answer exists
    while low <= high:
        mid = low + ((high - low) // 2)     # can be (low + high) // 2 but to avoid overflow, better to do like this; overflow - if high is INT_MAX then low + high will result in overflow
        if arr[mid] >= target:
            ans = mid   # possible answer; but we want smallest index, so go to the left side
            high = mid - 1
        else:
            low = mid + 1   # answer if exist will be on the right side
    return ans

arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
target = 9
print(lowerBound(arr, target))