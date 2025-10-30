# return whether the target is in the sorted matrix or not
# matrix is not sorted from [0][0] to [n][m]
# can only guarantee that each row is sorted and each column is sorted
# i.e., the last element in a row and the first element is the next row doesn't need to be sorted
# only row wise and column wise sorted

def searchInSortedMatrix2(mat, target):
    '''
    we need a sorted sequence pattern to do a binary search, in matrix case, to eliminate rows or cols
    if we see [0][0], everything to the right in the row is increasing and everything to the down in the column too is increasing
    if we see [n-1][m-1], everything to the up in the column is decreasing and everythin to the left in the row is too decreasing
    but if we see [0][m-1], everything to the left in the row is decreaing and everything to the down in the column is increasing.
    we see a sorted sequence here.
    Lets take the example,
    mat = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 14
    Lets start with [0][4]
    row = 0, col = 4:
        element = 15
        15 > 14, so we can say for sure that 14 can't be in the column 4, so eliminate column 4
        col -> 4 - 1 = 3
    row = 0, col = 3:
        ele = 11
        11 < 14     =>       can't be in the row, elimnate row    =>    row + 1 = 1
    row = 1, col = 3:
        ele = 12
        12 < 14  =>  can't be in the row     =>      row + 1 = 3
    row = 2, col = 3:
        ele = 16
        16 > 14     =>      can't be in the column      =>      col - 1 = 2
    row = 2, col = 2:
        ele = 9
        9 < 14      =>      can't be in the row     =>      row + 1 = 3
    row = 3, col = 2:
        ele = 14 = target
        found the element
    if we do like this, in worst case, we need to traverse from top right corner to bottom left corner
    and it would take n + m time to reach in this manner, so time complexity is O(n + m)

    we can achieve the same if we start from the bottom left corner too.

    we can wonder how binary search is used here. it is used here. the concept of elimination which is the core of binary search is used here
    '''
    n = len(mat)
    m = len(mat[0])
    row = 0
    col = m - 1
    while row < n and col >= 0:
        if mat[row][col] == target:
            return (True, [row, col])
        elif mat[row][col] < target:
            row += 1
        else:
            col -= 1
    return (False, [-1, -1])

mat = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 14
print(searchInSortedMatrix2(mat, target))