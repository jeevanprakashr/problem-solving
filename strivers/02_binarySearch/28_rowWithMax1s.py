# Given 2D array of 0's and 1's, find the row with maximum no. of 1's
# every row in the matrix is sorted
# if ans is multiple rows, return the smallest index row
# if no row have 1's, return -1

def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def rowWithMax1s(mat):
    '''
    brute: traverse the entire matrix and track the no. of ones for each row
    optimal:
    binary search
    Important: In matrix, we can't optimize the row traversal. We can only optimize how we traverse each row
    for each row, we use binary search to find the lower_bound(1) or upper_bound(0) or first_occurance(1)
    which gives us the index of starting 1 and with that we can find the no. of ones since the row is sorted
    m - no. of cols
    1's = m - index of first 1
    '''
    mxCnt = 0   # choosing 0 instead of -1 for the case if all elements in the matrix are 0 and we need to return -1 in this case
    index = -1
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        cnt = m - lowerBound(mat[i], m, 1)
        if cnt > mxCnt:
            mxCnt = cnt
            index = i
    return index


mat = [
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1]
]
print(rowWithMax1s(mat))