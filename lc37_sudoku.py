from time import time

def printBoard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

class Solution(object):
    def initDicts(self, board):
        self.horizontals = dict()
        self.verticals = dict()
        self.grids = dict()
        self.empties = []
        self.possibleNums = []
        for i in range(9):
            self.horizontals[i] = set()
            self.verticals[i] = set()
            self.grids[i] = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    self.horizontals[i].add(num)
                    self.verticals[j].add(num)
                    gridIdx = ((i // 3) * 3) + (j // 3)
                    self.grids[gridIdx].add(num)
                else:
                    self.empties.append((i, j))
        allNums = {str(i) for i in range(1, 10)}
        for i, j in self.empties:
            gridIdx = ((i // 3) * 3) + (j // 3)
            possi = allNums - (self.horizontals[i] & self.verticals[j] & self.grids[gridIdx])
            self.possibleNums.append(possi)
                    
    def isValid(self, board, row, col, num):
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
            if  board[startRow + (i // 3)][startCol + (i % 3)] == num:
                return False
        return True
    
    def solve3(self, emptyIdx, board):
        if emptyIdx == len(self.empties):
            return True
        row = self.empties[emptyIdx][0]
        col = self.empties[emptyIdx][1]
        gridIdx = ((row // 3) * 3) + (col // 3)
        '''siblingIndices = []
        for i in range(emptyIdx + 1, len(self.empties)):
            r = self.empties[i][0]
            c = self.empties[i][1]
            g = ((r // 3) * 3) + (c // 3)
            if r == row or c == col or g == gridIdx:
                siblingIndices.append(i)'''
        for i in self.possibleNums[emptyIdx]:
            si = str(i)
            if si not in self.horizontals[row] and si not in self.verticals[col] and si not in self.grids[gridIdx]:
                board[row][col] = si
                self.horizontals[row].add(si)
                self.verticals[col].add(si)
                self.grids[gridIdx].add(si)
                '''idxsOfRemovedSibs = []
                for idx in siblingIndices:
                    if si in self.possibleNums[idx]:
                        self.possibleNums[idx].remove(si)
                        idxsOfRemovedSibs.append(idx)'''
                if self.solve3(emptyIdx + 1, board):
                    return True
                else:
                    board[row][col] = "."
                    self.horizontals[row].remove(si)
                    self.verticals[col].remove(si)
                    self.grids[gridIdx].remove(si)
                    '''for idx in idxsOfRemovedSibs:
                        self.possibleNums[idx].add(si)'''
        return False
    
    def solve2(self, board, row, col):
        if row == 9:
            return True
        if col == 9:
            return self.solve2(board, row + 1, 0)
        if board[row][col] == ".":
            for i in range(1, 10):
                si = str(i)
                gridIdx = ((row // 3) * 3) + (col // 3)
                if si not in self.horizontals[row] and si not in self.verticals[col] and si not in self.grids[gridIdx]:
                    board[row][col] = si
                    self.horizontals[row].add(si)
                    self.verticals[col].add(si)
                    self.grids[gridIdx].add(si)
                    if self.solve2(board, row, col + 1):
                        return True
                    else:
                        board[row][col] = "."
                        self.horizontals[row].remove(si)
                        self.verticals[col].remove(si)
                        self.grids[gridIdx].remove(si)
                '''if self.isValid(board, row, col, str(i)):
                    board[row][col] = str(i)
                    if self.solve2(board, row, col + 1):
                        return True
                    else:
                        board[row][col] = "."'''
            return False
        else:
            return self.solve2(board, row, col + 1)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if self.isValid(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.initDicts(board)
        # self.solve(board)
        # self.solve2(board, 0, 0)
        self.solve3(0, board)

board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
# board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
s = Solution()
start = time()
s.solveSudoku(board)
total = time() - start
printBoard(board)
print(total)