# return whether the target is in the sorted matrix or not
# sorted from [0][0] to [n][m]

def searchInSortedMatrix(mat, target):
    '''
    Intuition is to apply binary search but how?
    If in case we flatten the matrix into 1D array then the time complexity will be O(log2(n*m))
    This is the minimum complexity that we can get
    but flattening itself will take O(n*m)
    So we need to skip flattening and do binary search on the matrix itself by considering 2d matrix into an 1d arr
    so
    low = 0
    high = (n*m) - 1
    we will get a 1D coordinate in binary search (as mid)
    we should convert this 1D coordinate into 2D coordinate somehow and formala for that is
    if n - rows and m - cols and x - 1D coordinate
    row = x // m
    col = x % m

    Eg:
    x = 5, n = 3, m = 4
    row = 5 // 4 = 1
    col = 5 % 4 = 1
    => [1][1]
    '''
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = (n * m) - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if mat[row][col] == target:
            return (True, mid)
        elif mat[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return (False, -1)
mat = [
    [3, 4, 7, 9],
    [12, 13, 16, 18],
    [20, 21, 23, 29]
]
target = 23
print(searchInSortedMatrix(mat, target))