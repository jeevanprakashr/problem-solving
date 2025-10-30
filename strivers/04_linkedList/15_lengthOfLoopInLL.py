# return length of loop if any exists else return 0
from LinkedList import Node, printLinkedList, getLinkedList

def lengthOfLoop(head):
    '''
    Intuition:
    Gonna use same tortoise and hare method as previous problems.
    If no intersecting point exists, return 0
    Else, from intersection point, move only one pointer forward and start counting. Once intersected again return the count.
    '''
    def findLength(slow, fast):
        cnt = 1
        fast = fast.nxt
        while slow != fast:
            cnt += 1
            fast = fast.nxt
        return cnt
    
    slow = head
    fast = head
    while fast and fast.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt
        if slow == fast:
            return findLength(slow, fast)
    return 0

head = Node(1, None)
temp = head
temp.nxt = Node(2, None)
temp = temp.nxt
temp.nxt = Node(3, None)
temp = temp.nxt
loopStart = temp
temp.nxt = Node(4, None)
temp = temp.nxt
temp.nxt = Node(5, None)
temp = temp.nxt
temp.nxt = Node(6, None)
temp = temp.nxt
temp.nxt = Node(7, None)
temp = temp.nxt
temp.nxt = Node(8, None)
temp = temp.nxt
temp.nxt = Node(9, None)
temp = temp.nxt
temp.nxt = loopStart
print(lengthOfLoop(head))
print(lengthOfLoop(getLinkedList([1, 2, 3, 4, 5])))