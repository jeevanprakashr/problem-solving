def rotateMatrix(mat):
    # nxn matrix
    n = len(mat)
    # Step 1: Transpose
    for i in range(n - 1):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # Step 2: Reverse rows
    for i in range(n):
        s = 0
        e = n - 1
        while s < e:
            mat[i][s], mat[i][e] = mat[i][e], mat[i][s]
            s += 1
            e -= 1

def printMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotateMatrix(mat)
printMatrix(mat)