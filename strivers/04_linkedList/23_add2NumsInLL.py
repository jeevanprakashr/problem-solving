# a linked list represents a number in reverse order
# given two linked lists, return the linked list with the sum in the same reverse order
from LinkedList import Node, printLinkedList, getLinkedList

def add2NumsInLL(head1, head2):
    dummy = Node(-1, None)
    curr = dummy
    t1 = head1
    t2 = head2
    carry = 0
    while t1 or t2:
        sm = carry
        if t1:
            sm += t1.data
        if t2:
            sm += t2.data
        node = Node(sm % 10, None)
        carry = sm // 10
        curr.nxt = node
        curr = node
        if t1:
            t1 = t1.nxt
        if t2:
            t2 = t2.nxt
    if carry:
        node = Node(carry, None)
        curr.nxt = node
    return dummy.nxt

head1 = getLinkedList([5, 4])
head2 = getLinkedList([3, 7, 9, 9])
res = add2NumsInLL(head1, head2)
printLinkedList(res)