class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addFront(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def addBack(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
    def removeFront(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            self.tail = None
            return
        newHead = self.head.next
        self.head.next = None
        newHead.prev = None
        self.head = newHead
    
    def removeBack(self):
        if not self.tail:
            return
        if not self.tail.prev:
            self.head = None
            self.tail = None
            return
        newTail = self.tail.prev
        self.tail.prev = None
        newTail.next = None
        self.tail = newTail
    
    def __str__(self):
        s = ""
        curr = self.head
        while curr:
            s += str(curr.data) + " "
            curr = curr.next
        return s


class Deque:
    def __init__(self):
        self.queue = DoublyLinkedList()
        self.size = 0
    
    def pushFront(self, ele):
        self.queue.addFront(ele)
        self.size += 1
    
    def pushBack(self, ele):
        self.queue.addBack(ele)
        self.size += 1
    
    def popFront(self):
        if self.size == 0:
            return
        popped = self.queue.head
        self.queue.removeFront()
        self.size -= 1
        return popped.data
    
    def popBack(self):
        if self.size == 0:
            return
        popped = self.queue.tail
        self.queue.removeBack()
        self.size -= 1
        return popped.data
    
    def topFront(self):
        if not self.queue.head:
            return
        return self.queue.head.data
    
    def topBack(self):
        if not self.queue.tail:
            return
        return self.queue.tail.data
    
    def isEmpty(self):
        return self.size == 0
    
    def __str__(self):
        return str(self.queue)