# return if the linked list is palindrome or not
from LinkedList import Node, printLinkedList, getLinkedList

def reverseLL(head):
    if not head or not head.nxt:
        return head
    prev = None
    curr = head
    while curr:
        temp = curr.nxt
        curr.nxt = prev
        prev = curr
        curr = temp
    return prev

def isPalindrome(head):
    '''
    Intuition:
    Reverse the second half of the linked list -> results tail as the new head
    To reverse - find the middle point using tortoise and hare method as in 10_middleOfLL
                 but this time get the first middle in case of even which means fast pointer should stop at
                 tail for odd
                 before tail for even
    After reversed and got tail as the new head of the second half, start comparing first half and reversed second half for palindrome
    '''
    slow = head
    fast = head
    while fast.nxt and fast.nxt.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt
    newHead = reverseLL(slow.nxt)
    first = head
    second = newHead
    while second:
        if first.data != second.data:
            reverseLL(newHead)
            return False
        first = first.nxt
        second = second.nxt
    reverseLL(newHead)
    return True

head = getLinkedList([1, 2, 3, 2, 1])
print(isPalindrome(head))
printLinkedList(head)