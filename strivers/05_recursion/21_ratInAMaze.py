# given a nxn grid having 0 and 1, give all possible paths rat would take to start from (0,0) and reach (n-1, n-1) via nodes of 1
# in string format containing D - down, U - up, R - right, L - left
# the possible paths should be ordered in lexicographical way

def getPathsForRat(maze):
    '''
    Since lexicographical order is needed, we can go in the order of D, L, R, U
    '''
    n = len(maze)
    visited = [[0 for i in range(n)] for j in range(n)]
    res = []
    if maze[0][0]:
        # collectPaths(0, 0, maze, n, "", res, visited)
        rowDir = [1, 0, 0, -1]
        colDir = [0, -1, 1, 0]
        collectPathsSimplified(0, 0, maze, n, res, "", visited, rowDir, colDir)
    return res

def collectPaths(row, col, maze, n, path, res, visited):
    if row == n - 1 and col == n - 1:
        res.append(path)
        return
    if row + 1 < n and not visited[row + 1][col] and maze[row + 1][col]:
        visited[row][col] = 1
        collectPaths(row + 1, col, maze, n, path + 'D', res, visited)
        visited[row][col] = 0
    
    if col - 1 >= 0 and not visited[row][col - 1] and maze[row][col - 1]:
        visited[row][col] = 1
        collectPaths(row, col - 1, maze, n, path + 'L', res, visited)
        visited[row][col] = 0
    
    if col + 1 < n and not visited[row][col + 1] and maze[row][col + 1]:
        visited[row][col] = 1
        collectPaths(row, col + 1, maze, n, path + 'R', res, visited)
        visited[row][col] = 0
    
    if row - 1 >= 0 and not visited[row - 1][col] and maze[row - 1][col]:
        visited[row][col] = 1
        collectPaths(row - 1, col, maze, n , path + 'U', res, visited)
        visited[row][col] = 0

def collectPathsSimplified(row, col, maze, n, res, path, visited, rowDir, colDir):
    '''
    Instead of doing the above if checks, we can combine them into single check
       rowDir   colDir
    D -  +1       +0
    L -  +0       -1
    R -  +0       +1
    U -  -1       +0
    '''
    if row == n - 1 and col == n - 1:
        res.append(path)
        return
    
    moves = "DLRU"
    for i in range(4):
        nextRow = row + rowDir[i]
        nextCol = col + colDir[i]
        if nextRow >= 0 and nextRow < n and nextCol >= 0 and nextCol < n and not visited[nextRow][nextCol] and maze[nextRow][nextCol]:
            visited[row][col] = 1
            collectPathsSimplified(nextRow, nextCol, maze, n, res, path + moves[i], visited, rowDir, colDir)
            visited[row][col] = 0
    
maze = [
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
print(getPathsForRat(maze))
    