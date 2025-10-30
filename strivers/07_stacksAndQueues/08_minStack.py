# Implement a stack with push, pop, top, size and along with these getMin too which gives the minimum in the stack
'''
Way to implement getMin is simple
Instead of just pushing the element into stack, we push it in a pair of element and the minimum element seen so far
eg: [12, 15, 10]  =>  [(12, 12), (15, 12), (10, 10)]
so when getMin is called, simply call the top and return the second value in the pair
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self, value):
        if self.size == 0:
            self.stack.append((value, value))
        else:
            pair = (value, min(value, self.getMin()))
            self.stack.append(pair)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.stack.pop()[0]
    
    def top(self):
        if self.size == 0:
            return
        return self.stack[self.size - 1][0]
    
    def getMin(self):
        if self.size == 0:
            return
        return self.stack[self.size - 1][1]

'''
The above implementation have O(1) tc for getMin but uses O(2n) for sc
This new implementation is to optimize so that tc stays as O(1) and sc becomes O(n)
Intuition:
we know that we need to track the minimum value every time we push into stack
But if we update the min, we lose the previous min as we can't store the history of min
So, when we face the situation that we need to update the min, we need to somehow incorporate the existing min
in the value to be pushed into the stack (i.e, to modify the value to be pushed into the stack)
For that, we use the formula
    (2 x val) - min = newVal
When top or pop called, we need to know whether the top value modified or not. For that
top < min => value modified, apply reverse formula 
else => value not modified
Derivation:
    we know, when the said situation occurs
    val < min
    =>  val - min       < 0
    =>  val + val - min < val
    =>  (2 x val) - min < val
    =>  newVal          < val
val is made as min and newVal is pushed into stack
so whenever a modification was made, we can say that the top of the stack (modified value) will always be lesser than min.
With this we can identify is modificaiton was made or not.
if min < top, no modification is made.
'''
class MinStack2:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.mini = 0
    
    def push(self, value):
        if self.size == 0:
            self.stack.append(value)
            self.mini = value
        else:
            if value > self.mini:
                self.stack.append(value)
            else:
                newVal = (2 * value) - self.mini
                self.stack.append(newVal)
                self.mini = value
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        x = self.stack.pop()
        if x > self.mini:
            return x
        top = self.mini
        self.mini = (2 * self.mini) - x
        return top
    
    def top(self):
        if self.size == 0:
            return
        x = self.stack[self.size - 1]
        if x > self.mini:
            return x
        return self.mini
    
    def getMin(self):
        if self.size == 0:
            return
        return self.mini
    
minStack = MinStack2()
minStack.push(12)
minStack.push(15)
minStack.push(10)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())