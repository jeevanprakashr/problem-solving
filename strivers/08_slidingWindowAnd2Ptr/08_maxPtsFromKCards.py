# given an array of numbers where each number represent a point of a card.
# given a number k
# return max points that can be gained by selecting k cards
# selecting cards should always be continuous and should always be from the start or from the end of the array
# sample: arr = [6, 2, 3, 4, 7, 2, 1, 7, 1], k = 4
# valid selections are
# left end = [6, 2, 3, 4]   right end = []
# left end = [6, 2, 3]      right end = [1]
# left end = [6, 2]         right end = [7, 1]
# left end = [6]            right end = [1, 7, 1]
# left end = []             right end = [2, 1, 7, 1]

def maxPtsFromKCards(arr, k):
    '''
    if we look at it, this is sliding window problem but the window is split between beginning and end of the array
    the above explained method is the optimal solution and simply understandable
    '''
    lsum = 0
    rsum = 0
    mxSum = 0
    for i in range(k):
        lsum += arr[i]
        mxSum = lsum
    rIdx = len(arr) - 1
    for i in range(k - 1, -1, -1):
        lsum -= arr[i]
        rsum += arr[rIdx]
        total = lsum + rsum
        mxSum = max(mxSum, total)
        rIdx -= 1
    return mxSum

arr = [6, 2, 3, 4, 7, 2, 1, 7, 1]
k = 4
print(maxPtsFromKCards(arr, k))
