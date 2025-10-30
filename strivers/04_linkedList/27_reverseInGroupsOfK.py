# given linked list and k, reverse nodes in groups of k
# Eg: 1, 2, 3, 4, 5, 6, 7, 8 and k = 3  =>  3, 2, 1, 6, 5, 4, 7, 8
# If there are nodes less than k, don't reverse it
from LinkedList import Node, printLinkedList, getLinkedList

def getKthNode(head, k):
    temp = head
    k -= 1
    while temp and k > 0:
        temp = temp.nxt
        k -= 1
    return temp

def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.nxt
        curr.nxt = prev
        prev = curr
        curr = temp
    return prev

def reverseInGrpsOfK(head, k):
    temp = head
    prev = None
    nxt = None
    while temp:
        kthNode = getKthNode(temp, k)
        if not kthNode:
            if prev:
                prev.nxt = temp
            break
        nxt = kthNode.nxt
        kthNode.nxt = None
        reverse(temp)
        if temp == head:
            head = kthNode
        else:
            prev.nxt = kthNode
        prev = temp
        temp = nxt
    return head

head = getLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
newHead = reverseInGrpsOfK(head, 3)
printLinkedList(newHead)
