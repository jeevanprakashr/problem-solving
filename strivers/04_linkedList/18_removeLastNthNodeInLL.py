# remove nth node from the last in the linked list
from LinkedList import Node, printLinkedList, getLinkedList

def removeLastNth(head, n):
    '''
    Intuition:
    Start a fast pointer from head and move n steps
    when fast pointer did n steps, start a slow pointer from head and this time move both a single step
    when fast pointer reached the tail, the slow pointer will be at the n-1 th node from the last
    '''
    fast = head
    for i in range(n):
        fast = fast.nxt
    if not fast:
        # asked to remove head node
        return head.nxt
    slow = head
    while fast.nxt:
        slow = slow.nxt
        fast = fast.nxt
    slow.nxt = slow.nxt.nxt
    return head

head = getLinkedList([1, 2, 3, 4, 5])
n = 2
newHead = removeLastNth(head, n)
printLinkedList(newHead)