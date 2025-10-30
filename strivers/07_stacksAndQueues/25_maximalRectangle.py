# given an nxm matrix of 0s and 1s, return the maximum area of rectangle that contains only 1s
# sample: arr = [
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 1],
#   [1, 1, 1, 1, 1],
#   [1, 0, 0, 1, 0]
# ]
# ans = 6

from Stack import Stack

def maximalRectangle(mat):
    '''
    If we look at it, we can realize that the previous largestRectInHistogram can be applied here
    How:
    If we consider each row as the base of the histogram and construct bars of height based on continuous 1s above from the base
    it would look like an histogram we saw in our previous problem.
    We can find the maximum rectangle area of this histogram and track the max area.
    If we follow the same for each row from top to bottom while tracking max area, we find our answer
    As for computing heights at each row, we can use prefixSum concept to convert the matrix. Lets consider the above example,
    the computed heights matrix would like
    [
        [1, 0, 1, 0, 1],
        [2, 0, 2, 1, 2],
        [3, 1, 3, 2, 3],
        [4, 0, 0, 3, 0]
    ]
    we need to reset the prefix sum if we encounter a 0 in the column bar.
    '''
    n = len(mat)
    m = len(mat[0])
    prefixSum = [[0 for i in range(m)] for j in range(n)]
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += mat[i][j]
            if mat[i][j] == 0:
                sum = 0
            prefixSum[i][j] = sum
    
    maxArea = 0
    for i in range(n):
        maxArea = max(maxArea, largestRectInHistogram(prefixSum[i]))
    return maxArea

def largestRectInHistogram(arr):
    n = len(arr)
    st = Stack()
    maxArea = 0
    for i in range(n):
        while not st.isEmpty() and arr[st.top()] > arr[i]:
            idx = st.pop()
            nse = i
            pse = -1 if st.isEmpty() else st.top()
            area = arr[idx] * (nse - pse - 1)
            maxArea = max(area, maxArea)
        st.push(i)
    while not st.isEmpty():
        idx = st.pop()
        nse = n
        pse = -1 if st.isEmpty() else st.top()
        area = arr[idx] * (nse - pse - 1)
        maxArea = max(area, maxArea)
    return maxArea

mat = [
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0]
]
print(maximalRectangle(mat))