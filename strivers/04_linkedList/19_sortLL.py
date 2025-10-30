# sort the given linked list
from LinkedList import Node, printLinkedList, getLinkedList
def sortLL(head):
    '''
    We are going to use merge sort here. For merge sort, we need middle node to separate left and right halves
    For that we use tortoise and hare method.
    But that method will give second middle in case of even nodes. We do a slight modification to it.
    We start fast pointer at the head's next node instead of head to get first middle
    '''
    def middleNode(head):
        if not head or not head.nxt:
            return head
        slow = head
        fast = head.nxt
        while fast and fast.nxt:
            slow = slow.nxt
            fast = fast.nxt.nxt
        return slow
    
    def merge2LL(l1, l2):
        dummyNode = Node(-1, None)
        temp = dummyNode
        while l1 and l2:
            if l1.data < l2.data:
                temp.nxt = l1
                temp = l1
                l1 = l1.nxt
            else:
                temp.nxt = l2
                temp = l2
                l2 = l2.nxt
        if l1:
            temp.nxt = l1
        else:
            temp.nxt = l2
        return dummyNode.nxt
    
    if not head or not head.nxt:
        return head
    middle = middleNode(head)
    leftHead = head
    rightHead = middle.nxt
    middle.nxt = None
    leftHead = sortLL(leftHead)
    rightHead = sortLL(rightHead)
    return merge2LL(leftHead, rightHead)

head = getLinkedList([3, 5, 2, 1, 4])
newHead = sortLL(head)
printLinkedList(newHead)