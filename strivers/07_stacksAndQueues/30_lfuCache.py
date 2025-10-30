# implement lfu cache which uses O(1) TC for put and get
# lfu = least frequently used
# if more than one lfu element, (a tie occured) use lru there

'''
we use a map to store frequency vs its lru linked list as we saw in previous lruCache implementation
we track least frequency
if frequency is increased and older frequency is the current frequency, check older frequency's lru size, if empty increase least frequency
if new element added, make least frequency back to 1
similar to lru we maintain map to store key vs node
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

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

class LRUCache:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

class LFUCache:
    def __init__(self, capacity):
        self.nodeMap = dict()
        self.freqMap = dict()
        self.capacity = capacity
        self.leastFreq = 0
    
    def put(self, key, val):
        if key in self.nodeMap:
            node = self.nodeMap[key]
            deleteNode(node)
            prevLruCache = self.freqMap[node.freq]
            prevLruCache.size -= 1
            if prevLruCache.size == 0:
                self.freqMap.pop(node.freq, None)
                if node.freq == self.leastFreq:
                    self.leastFreq += 1
            node.freq += 1
            lruCache = None
            if node.freq in self.freqMap:
                lruCache = self.freqMap[node.freq]
            else:
                lruCache = LRUCache()
                self.freqMap[node.freq] = lruCache
            insertAfterHead(lruCache.head, node)
            lruCache.size += 1
            node.value = val
        else:
            if len(self.nodeMap) == self.capacity:
                lruCache = self.freqMap[self.leastFreq]
                lruNode = lruCache.tail.prev
                deleteNode(lruNode)
                lruCache.size -= 1
                if lruCache.size == 0:
                    self.freqMap.pop(lruNode.freq, None)
                self.nodeMap.pop(lruNode.key, None)
            self.leastFreq = 1
            lruCache = None
            if 1 in self.freqMap:
                lruCache = self.freqMap[1]
            else:
                lruCache = LRUCache()
                self.freqMap[1] = lruCache
            node = Node(key, val)
            insertAfterHead(lruCache.head, node)
            lruCache.size += 1
            self.nodeMap[key] = node
    
    def get(self, key):
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        deleteNode(node)
        lruCache = self.freqMap[node.freq]
        lruCache.size -= 1
        if lruCache.size == 0:
            self.freqMap.pop(node.freq, None)
            if node.freq == self.leastFreq:
                self.leastFreq += 1
        node.freq += 1
        lruCache = None
        if node.freq in self.freqMap:
            lruCache = self.freqMap[node.freq]
        else:
            lruCache = LRUCache()
            self.freqMap[node.freq] = lruCache
        insertAfterHead(lruCache.head, node)
        lruCache.size += 1
        return node.value