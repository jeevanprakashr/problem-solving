class Node:
    def __init__(self, data, nxt):
        self.data = data
        self.nxt = nxt
    
    def __str__(self):
        return str(self.data) + " " + str(self.nxt != None)

def getLinkedList(arr):
    head = None
    n = len(arr)
    if n == 0:
        return None
    head = Node(arr[0], None)
    curr = head
    for i in range(1, n):
        temp = Node(arr[i], None)
        curr.nxt = temp
        curr = temp
    return head

def printLinkedList(head):
    curr = head
    while curr:
        print(curr)
        curr = curr.nxt