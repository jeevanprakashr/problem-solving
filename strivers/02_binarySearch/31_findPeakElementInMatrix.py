# refer 12_findPeakElement
# 2 adjacent cells are not same
# here peak element is greater than its left, right, top and bottom adjacent cells
# all outer parts out of the matrix are -1
# can be many peaks, return one of them
def findPeakElementInMatrix(mat):
    '''
    Intuition:
    we can do binary search on either rows or cols
    lets do in cols (0 to m - 1)
    once we find mid in cols, we find max element in that col (to be precise, find row index containing the max element in that col)
    since it is the max element it is already greater than top and bottom
    if left and right is lesser:
        current element is a peak and return it
    if left is greater:
        we know peak lies on the left side. left may be a peak, or may not.
        if left is not a peak, we know for sure that any greater element on top or bottom of the left will definitely be greater than our current col
        since we are looking at the max of the current col.
        so we eliminate the right
    else:
        same concept, eliminate the left
    '''
    def maxRowIndex(col):
        mx = -1
        index = -1
        for i in range(n):
            if mat[i][col] > mx:
                mx = mat[i][col]
                index = i
        return index
    
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = m - 1
    while low <= high:
        mid = (low + high) // 2
        mxRow = maxRowIndex(mid)
        left = mat[mxRow][mid - 1] if mid - 1 >= 0 else -1
        right = mat[mxRow][mid + 1] if mid + 1 < m else -1
        curr = mat[mxRow][mid]
        if curr > left and curr > right:
            return (curr, (mxRow, mid))
        elif curr < left:
            high = mid - 1
        else:
            low = mid + 1
    return (-1, (-1, -1))

mat = [
    [4, 2, 5, 1, 4, 5],
    [2, 9, 3, 2, 3, 2],
    [1, 7, 6, 0, 1, 3],
    [3, 6, 2, 3, 7, 2]
]
print(findPeakElementInMatrix(mat))