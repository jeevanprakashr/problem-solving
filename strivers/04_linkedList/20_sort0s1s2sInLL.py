# sort linked list of 0s, 1s and 2s
from LinkedList import Node, printLinkedList, getLinkedList

def sort0s1s2s(head):
    if not head or not head.nxt:
        return head
    zeroHead = Node(-1, None)
    oneHead = Node(-1, None)
    twoHead = Node(-1, None)
    zero = zeroHead
    one = oneHead
    two = twoHead
    temp = head
    while temp:
        if temp.data == 0:
            zero.nxt = temp
            zero = temp
        elif temp.data == 1:
            one.nxt = temp
            one = temp
        else:
            two.nxt = temp
            two = temp
        temp = temp.nxt
    zero.nxt = oneHead.nxt if oneHead.nxt else twoHead.nxt
    one.nxt = twoHead.nxt
    two.nxt = None
    newHead = zeroHead.nxt
    return newHead

head = getLinkedList([1, 0, 2, 1, 1, 0, 2])
newHead = sort0s1s2s(head)
printLinkedList(newHead)