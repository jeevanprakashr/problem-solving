# given nxn grid, arrange n queens, so that
# each row has 1 queen
# each col has 1 queen
# without attacking each other

def solveNQueens(n):
    '''
    same recursion and backtracking as we did before
    select each col and place queen in each row, if it satisfies "call" (recusion) for next col or else "iterate" (loop inside recusion) to next row
    to check if its safe maintain hash arrays
    since we place queens from left col to right col, no need to check right side or right upper and lower diagonal
    since we place only one queen per col, no need to check for up or down directions
    only check left row, left upper and left lower diagonal
    left row - hash array of length n
    since there are 2n - 1 diagonals for a nxn grid, the diagonal hash arrays will be of length 2n - 1
    lower diagonal formula = row + col
    upper diagonal formula = n - 1 + col - row    =>  since (col - row) will result in [-(n - 1), -(n - 2), ..., 0, ..., n - 2, n - 1], to negate negatives (n - 1) is added
    '''
    board = [['.' for i in range(n)] for j in range(n)]
    leftRow = [0 for _ in range(n)]
    upperDiagonal = [0 for _ in range(2 * n - 1)]
    lowerDiagonal = [0 for _ in range(2 * n - 1)]
    res = []
    solve(0, board, res, leftRow, upperDiagonal, lowerDiagonal, n)
    return res


def solve(col, board, res, leftRow, upperDiagonal, lowerDiagonal, n):
    if col == n:
        copy = []
        for row in board:
            copy.append(list(row))
        res.append(copy)
        return
    for row in range(n):
        if leftRow[row] == 0 and upperDiagonal[n - 1 + col - row] == 0 and lowerDiagonal[col + row] == 0:
            board[row][col] = 'Q'
            leftRow[row] = 1
            upperDiagonal[n - 1 + col - row] = 1
            lowerDiagonal[col + row] = 1

            solve(col + 1, board, res, leftRow, upperDiagonal, lowerDiagonal, n)

            lowerDiagonal[col + row] = 0
            upperDiagonal[n - 1 + col - row] = 0
            leftRow[row] = 0
            board[row][col] = '.'

n = 4
res = solveNQueens(n)
for board in res:
    for row in board:
        print(row)
    print()
print(len(res))