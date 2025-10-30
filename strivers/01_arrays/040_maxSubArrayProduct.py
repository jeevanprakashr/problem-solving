def maxSubArrayProduct(arr):
    '''
    Intuition:
    Case 1: if all elements are +ve, then the entire array is the answer
    Case 2: if there are even number of -ve, then also entire array is the answer
    Case 3: odd number of -ve
        Removal of one -ve will make the entire array positive. so we need to see which 1 -ve to remove
        for each -ve, find prefix product and suffix product to it and take the maximum
        do the same for all -ve and take the max
    Case 4: arr contains 0
        whenever we see prefix or suffix as 0 as a result of multiplying with a 0, reset it to 1, since 0 can't be in a subarray
        and whatever subarray we kept building up either prefix subArr or suffix subArr ends before that 0 and after it
        a new subarray starts
    '''
    n = len(arr)
    prefix = 1
    suffix = 1
    res = float("-inf")
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix = prefix * arr[i]
        suffix = suffix * arr[n - i - 1]
        res = max(res, max(prefix, suffix))
    return res

arr = [2, 3, -2, 4]
arr = [3, 2, -1, 4, -6, 3, -2, 6]
arr = [-2, 4, 5, 6, -7]
arr = [-2, 4, 5, 6, -7, -1]
arr = [-2, 3, 4, -1, 0, -2, 3, 1, 4, 0, 4, 6, -1, 4]
print(maxSubArrayProduct(arr))