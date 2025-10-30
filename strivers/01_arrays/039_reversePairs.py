# reverse pair - a pair (arr[i], arr[j]) where arr[i] > 2 * arr[j], i < j
def countReversePairs(arr):
    '''
    We will use merge sort in a similar way to 038_countInversions but not as exactly the same
    Reason:
    For eg, arr1 = [6, 13, 21, 25]    arr2 = [1, 2, 3, 4, 4, 5, 9, 11, 13]
    lets left = 6, right = 3
    if we follow the same pattern as countInversions
    (6, 3) is not a reverse pair and hence we move right to 4 according to merge algo
    but by doing so, we miss (13, 3), (21, 3) and (25, 3)

    Intuition:
    for 6  - [1, 2] form pairs
    for 13 - [1, 2, 3, 4, 4, 5]
    for 21 - [1, 2, 3, 4, 4, 5, 9]
    for 25 - [1, 2, 3, 4, 4, 5, 9, 11]

    Inference:
    if [1, 2] form pair with 6 then it also form pairs with all other elements greater than 6 in left arr

    Logic:
    1. left - 6; right - 1
        forms pair, increment right
    2. (6, 2)
        forms pair, increment right
    3. (6, 3)
        not a pair, so count is 2 (right + 1)
        increment left
    4. (13, 3)
        forms pair, incremnet right and goes upto 9
    .
    .
    .
    x. (13, 9)
        not a pair, so add 6 to existing count
        count = 2 + 6 = 8
    and goes on

    This logic is a separate on. Not comes inside merging algo as before
    This logic comes after spliting and before merging
    '''
    def countPairs(arr, low, mid, high):
        cnt = 0
        right = mid + 1
        for left in range(low, mid + 1):
            while right <= high and arr[left] > 2 * arr[right]:
                right += 1
            cnt += right - (mid + 1)
        return cnt

    def merge(arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
    
    def mergeSort(arr, low, high):
        revPairs = 0    # logic for our solution
        if low >= high:
            return revPairs     # logic for our solution
        mid = (low + high) // 2
        revPairs += mergeSort(arr, low, mid)
        revPairs += mergeSort(arr, mid + 1, high)
        revPairs += countPairs(arr, low, mid, high)    # logic for our solution
        merge(arr, low, mid, high)
        return revPairs     # logic for our solution
    
    n = len(arr)
    return mergeSort(arr, 0, n - 1)

arr = [40, 25, 19, 12, 9, 6, 2]
# arr = [6, 13, 21, 25, 1, 2, 3, 4, 4, 5, 9, 11, 13]
print(countReversePairs(arr))
print(arr)