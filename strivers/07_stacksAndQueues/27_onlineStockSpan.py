# complete a function "next" to which the current price of a stock will be passed on each day
# make this function return an integer which would give the no. of past consecutive days
# starting from the current day on which the price is lesser than or equal to the current price
'''
sample:
StockSpanner -> start of a stock
next - 7    no. of days <= 7 = 1
next - 2    no. of days <= 2 = 1
next - 1    no. of days <= 1 = 1
next - 3    no. of days <= 3 = 3  (2, 1, 3)
next - 3    no. of days <= 3 = 4  (2, 1, 3, 3)
next - 1    no. of days <= 1 = 1
next - 8    no. of days <= 8 = 7  (7, 2, 1, 3, 3, 1, 8)
'''

from Stack import Stack

class StockSpanner:
    '''
    let see the above example
    [7, 2, 1, 3, 3, 1, 8]
    for first occuring 3, 
    next(3) = 3
    which is idx [1 to 3]
    we can see that the solution for this is previousGreaterElement
    i.e
    next(ele) = curr ele's idx - idx(pge(ele))
    next(3) = 3 - idx(7) = 3 - 0 = 3
    '''
    def __init__(self):
        # elements in stack will in form of (val, idx)
        self.stack = Stack()
        self.idx = -1
    
    def next(self, val):
        self.idx += 1
        while not self.stack.isEmpty() and self.stack.top()[0] <= val:
            self.stack.pop()
        res = self.idx - (-1 if self.stack.isEmpty() else self.stack.top()[1])
        self.stack.push((val, self.idx))
        return res

sol = StockSpanner()
print(sol.next(7))
print(sol.next(2))
print(sol.next(1))
print(sol.next(3))
print(sol.next(3))
print(sol.next(1))
print(sol.next(8))