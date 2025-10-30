class SetMatrixZeros:
    '''
    Change all 1's in 0 occuring rows and cols to 0's
    [[1, 1, 1, 1],          [[ 0,  0,  0,  1],
     [1, 0, 1, 1],           [ 0, "0", 0,  0],
     [1, 1, 0, 1],  --->     [ 0,  0, "0", 0],
     [0, 1, 1, 1]]           ["0", 0,  0,  0]]
    '''
    def better(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        rows = [0 for _ in range(n)]
        cols = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(n):
            for j in range(m):
                if rows[i] == 1 or cols[j] == 1:
                    matrix[i][j] = 0
    
    def optimal(self, matrix):
        # rows = matrix[0 to n][0]
        # cols = col0 + matrix[0][1 to m]
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(1, m):
                matrix[0][i] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

def printMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

matrix = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 1]]
sol = SetMatrixZeros()
# sol.better(matrix)
sol.optimal(matrix)
printMatrix(matrix)