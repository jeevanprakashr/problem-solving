class PascalTriangle:
    '''
    0 -           1
    1 -         1   1
    2 -       1   2   1                      2C1
    3 -     1   3   3   1                 3C1   3C2
    4 -   1   4   6   4   1            4C1   4C2   4C3
    5 - 1   5  10  10   5   1       5C1   5C2   5C3   5C4

    nCr = n! / (r! * (n - r)!)

    Eg: No. of ways to select 3 books from 5 books - 5C3
    Note: order is not mattered - nCr; order matters - plain combinations (5 x 4 x 3)

    Q1: Given row and col, return the element from pascal triangle
    Q2: Return nth row
    Q3: Given n, eturn entire n-length pascal triangle
    '''
    def question1(self, row, col):
        def nCr(n, r):
            '''
            Intuition:
            5C2 = 5! / (2! * (5 - 2)!)
                = 5! / (2! * 3!)
                = 5 * 4 * (3 * 2 * 1) / 2 * 1 * (3 * 2 * 1)   =>   (3 * 2 * 1) always cancel each other
            So 5C2 can be written as
            5C2 = (5 * 4) / (1 * 2)   =>   always best to multiply elements in ascending order in denominator
                = (5 / 1) * (4 / 2)
            '''
            res = 1
            for i in range(r):
                res = res * (n - i)
                res = res // (i + 1)
            return res
        return nCr(row - 1, col - 1)     # row and col is not 0-index based
    
    def question2(self, row):
        def generateRow(row):
            '''
            Intuition:
            row = 6 (6th row)
            nth row has n elements
            1  5  10  10  5  1

            1   5   5 x 4   5 x 4 x 3   5 x 4 x 3 x 2   5 x 4 x 3 x 2 x 1
                -   -----   ---------   -------------   -----------------
                1   1 x 2   1 x 2 x 3   1 x 2 x 3 x 4   1 x 2 x 3 x 4 x 5
            
            We can see a dependency between elements. nth element can be obtained for n-1th element
            '''
            ansRow = [1]
            res = 1
            for i in range(1, row):
                res = res * (row - i)
                res = res // i
                ansRow.append(res)
            return ansRow
        return generateRow(row)
    
    def question3(self, n):
        def generateRow(row):
            ansRow = [1]
            res = 1
            for i in range(1, row):
                res = res * (row - i)
                res = res // i
                ansRow.append(res)
            return ansRow
        
        triangle = []
        for i in range(1, row + 1):
            triangle.append(generateRow(i))
        return triangle

sol = PascalTriangle()
row = 6
col = 3
print(sol.question1(row, col))
print()
print(sol.question2(row))
print()
for row in sol.question3(6):
    print(row)

    
