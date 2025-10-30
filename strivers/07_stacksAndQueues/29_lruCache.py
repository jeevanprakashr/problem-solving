# implement lru cache which uses O(1) TC for put and get

'''
Use doubly linked list and map to implement lru cache
head - most recent node
any new put will be added to tail
'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"
    
def deleteNode(node):
    front = node.prev
    back = node.next
    node.prev = None
    node.next = None
    front.next = back
    back.prev = front

def insertAfterHead(head, node):
    recent = head.next
    head.next = node
    node.prev = head
    node.next = recent
    recent.prev = node

def printDLL(head):
    curr = head
    while curr:
        print((curr.key, curr.value), end=" ")
        curr = curr.next
    print()

def printMap(d):
    for k in d:
        print(k, str(d[k]), end=" ")
    print()

class LRUCache:
    def __init__(self, capacity):
        self.map = dict()
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def put(self, key, val):
        if key in self.map:
            node = self.map[key]
            deleteNode(node)
            insertAfterHead(self.head, node)
            node.value = val
        else:
            if len(self.map) == self.capacity:
                leastRecent = self.tail.prev
                deleteNode(leastRecent)
                self.map.pop(leastRecent.key, None)
            node = Node(key, val)
            insertAfterHead(self.head, node)
            self.map[key] = node
    
    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        deleteNode(node)
        insertAfterHead(self.head, node)
        return node.value
    
lruCache = LRUCache(4)
lruCache.put(2, 6)
lruCache.put(4, 7)
lruCache.put(8, 11)
lruCache.put(7, 10)
print(lruCache.get(2))
print(lruCache.get(8))
lruCache.put(5, 6)
print(lruCache.get(7))

