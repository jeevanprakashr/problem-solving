def maxSubArraySum(arr):
    # Kadane's algorithm
    # add up each element while iterating.
    # if sum is negative, reset it to 0, since it will only depreciate the upcoming element.
    # if sum is positive, keep it, since it will appreciate the next element even the next element
    # might be negative, hoping it will come in handy in future.
    sm = 0
    maxi = float("-inf")
    n = len(arr)
    start = -1
    ansStart = -1  # start and end indices of the answer sub array
    ansEnd = -1
    for i in range(n):
        if sm == 0:
            start = i
        sm += arr[i]
        if sm > maxi:
            maxi = sm
            ansStart = start
            ansEnd = i
        if sm < 0:
            sm = 0
    if maxi < 0:
        return 0   # Empty sub array
    print(ansStart, ansEnd)
    return maxi

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(arr))