class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self, val):
        self.stack.append(val)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.stack.pop()
    
    def top(self):
        if self.size == 0:
            return
        return self.stack[self.size - 1]
    
    def isEmpty(self):
        return self.size == 0