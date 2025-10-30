# given nxn matrix of 0/1
# mat[i][j] = 1  =>  i-th person "knows" j-th person, not vice versa
#           = 0  =>  i-th person "doesn't know" j-th person, not vice versa
# there can be
# mat[i][j] = 0 and
# mat[j][i] = 1
# which means i knows j, but j doesn't know i
# celebrity - everyone knows him but he knows no one
# sample:
# [[0, 1, 1, 0],
#  [0, 0, 0, 0],
#  [0, 1, 0, 0],
#  [1, 1, 0, 0]]
# ans = person 1 (index 1)  =>  mat[1][0-3] = 0 and mat[0,2,3][1] = 1
# fact: there can be either one celebrity or no celebrity at all

def celebrityProblem(mat):
    '''
    Solution 1:
    compute knowsMe and iKnow arrays for persons 0 to n - 1
    knowsMe[i] = no. of persons who knows i
    iKnow[i] = no. of persons known by i
    traverse matrix and for mat[i][j]
    if 1:
        i knows j -> knowsMe[j] += 1
                  -> iKnow[i] += 1
    if knowsMe[i] is n - 1 and iKnow[i] is 0, then i is our answer
    This uses
    TC: O(n^2 + n)
    SC: O(2n)

    Solution 2:
    Optimal approach is using two pointer sort of solution
    have two pointers top and down
    top = 0
    down = n-1
    => if top knows down, top can't be celebrity -> increment top
    => if down knows top, down can't be celebrity -> decrement down
    => if both don't know each other, both of them can'b celebrity as celebrity must be known by all -> increment top and decrement down
    one of these 3 conditions would pass and thus move pointers
    if top and down coincides, check whether that person is celebrity and return result
    if top and down crosses each other then there is no celebrity
    '''
    n = len(mat)
    top = 0
    down = n - 1
    while top < down:
        if mat[top][down] == 1:
            top += 1
        elif mat[down][top] == 1:
            down -= 1
        else:
            top += 1
            down -= 1
    if top > down:
        return -1
    for i in range(n):
        if i == top:
            continue
        if mat[i][top] == 1 and mat[top][i] == 0:
            continue
        else:
            return -1
    return top

mat = [
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(celebrityProblem(mat))