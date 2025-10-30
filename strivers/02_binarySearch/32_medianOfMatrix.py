# Given 2D array of size n x m, where both n and m are odd numbers (fact: product of two odd numbers is also an odd number)
# sorted only in row wise
# neither in col wise nor entire matrix from 0, 0 to n-1, m-1
# median - middle value in a sorted set of numbers

def medianOfMatrix(mat):
    '''
    Intuition:
    Let's take the example,
    mat = [
        [1, 5, 7, 9, 11],
        [2, 3, 4, 5, 10],
        [9, 10, 12, 14, 16]
    ]
    Lets say the matrix is flattened and sorted.
    [1, 2, 3, 4, 5, 5, 7, 9, 9, 10, 10, 11, 12, 14, 16]

    The answer definitely would be between the smallest and the largest number
    So the search space would be between smallest and largest
    i.e, between 1 and 16

    We know that for the median the no of element to the left and right would be equal and in this case 7
    i.e there are 7 elements to the left of 9 (median)

    Let's track the no of elements "<=" itself for 1 to 16
    reason for "<=" : suppose we have 7 instead of 9 in the median place
                      the no of elements less than 7 on the left would be only 6 [1, 2, 3, 4, 5, 5]
                      and the 7 beside the median 7 was left behind
                      and according to the fact that median should have 7 elements to the left, our 7 wouldn't be the answer
                      but in actual, it is the answer, hence "<="
    So any element which has more than 7 elements lesser or equal to itself can be a median
    reason for more than 7: what if the actual median repeats itself after the median position to the right side as 9 in our case
    =>     condition = no. of "<=" elements(element) > 7
    Search space:           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                             |  |  |  |  |  |  |  |  |  |   |   |   |   |   |   |
    No. of "<=" elements:   [1, 2, 3, 4, 6, 6, 7, 7, 9, 11, 12, 13, 13, 14, 14, 15]
                             x  x  x  x  x  x  x  x  o  o   o   o   o   o   o   o
    
    Now we got a binary search pattern
    The first occurance of no. of "<=" elements which is greater than 7 is our answer
    Here the first occurence is 9 which corresponds to the element 9
    search space = 1 to 16
    if we got "<=Elements" of mid lesser or equal to 7 -> move right
    else -> move left (as we want first occurence (minimum))
    '''
    def upperBound(row, target):
        # upper bound - first element larger than the target
        # return its index which can be used to tell the no. of elements "<=" target
        low = 0
        high = m - 1
        ansIndex = m
        while low <= high:
            mid = (low + high) // 2
            if row[mid] > target:
                ansIndex = mid
                high = mid - 1
            else:
                low = mid + 1
        return ansIndex
    
    def lesserEqual(element):
        cnt = 0
        for i in range(n):
            cnt += upperBound(mat[i], element)
        return cnt
    
    n = len(mat)
    m = len(mat[0])
    left = (n * m) // 2
    low = float("+inf")
    high = float("-inf")
    for i in range(n):
        low = min(low, mat[i][0])
        high = max(high, mat[i][m - 1])
    while low <= high:
        mid = (low + high) // 2
        lesserEqualEles = lesserEqual(mid)
        if lesserEqualEles <= left:
            low = mid + 1
        else:
            high = mid - 1
    return low

mat = [
    [1, 5, 7, 9, 11],
    [2, 3, 4, 5, 10],
    [9, 10, 12, 14, 16]
]
print(medianOfMatrix(mat))