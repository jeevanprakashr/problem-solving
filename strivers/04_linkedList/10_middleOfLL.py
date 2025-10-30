from LinkedList import getLinkedList, printLinkedList

# Return the middle node of the linked list
# if odd - middle, if even - second middle ((n / 2) + 1)

def middleNode(head):
    '''
    Tortoise Hare algorithm
    two pointer - slow and fast
    for each iteration
    - slow jumps 1 step
    - fast jumps 2 steps
    when fast is at tail node (even) or none/null (odd) - slow will be at middle, return slow
    '''
    slow = head
    fast = head
    while fast and fast.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt
    return slow

head = getLinkedList([1, 2, 3, 4, 5])
middle = middleNode(head)
print(middle)

head = getLinkedList([1, 2, 3, 4, 5, 6])
middle = middleNode(head)
print(middle)