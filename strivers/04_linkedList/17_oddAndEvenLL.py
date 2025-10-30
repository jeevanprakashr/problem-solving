# Group odd and even index nodes together and return the new linked list
# Eg: Given [1, 3, 4, 2, 5, 6]   return  [1, 4, 5, 3, 2, 6]     odd nodes followed by even nodes
from LinkedList import Node, printLinkedList, getLinkedList

def groupOddAndEvenNodes(head):
    '''
    Start two pointers from 1st (oddHead) and 2nd (evenHead) nodes
    Jump 2 steps and change links while doing it (even pointer will always be at the end after completing this step)
    point last odd pointer to evenHead
    '''
    if not head or not head.nxt:
        return head
    odd = head
    even = head.nxt
    evenHead = head.nxt
    while even and even.nxt:
        odd.nxt = odd.nxt.nxt
        even.nxt = even.nxt.nxt
        odd = odd.nxt
        even = even.nxt
    odd.nxt = evenHead
    return head

head = getLinkedList([1, 2, 3, 4, 5])
groupOddAndEvenNodes(head)
printLinkedList(head)