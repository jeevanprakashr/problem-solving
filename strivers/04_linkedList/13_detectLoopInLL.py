from LinkedList import Node, printLinkedList, getLinkedList

def detectLoop(head):
    '''
    Better approach is to use hashing to store nodes in and check for visited
    Optimal:
    Using tortoise and hare approach as in 10_middleOfLL
    When the slow and fast pointer meet each other or equal, then there is a loop
    Reason:
    when both the slow and fast pointers enter the looped segment, fast pointer tries to reach/overtake slow pointer and
    slow pointer tries to get away from fast pointer
    This causes the distance between fast and slow pointer (fast towards slow) to decrease in each iteration by 1
    The reason for 1 is fast jumps 2 steps towards slow while slow jumps 1 step to get away from fast which results the diff of 1
    And since the decrease is by 1 in each iteration, the intersection of slow and fast pointers is bound to happen at some point, thus detecting the loop
    This is the reason for choosing the fact that fast moves 2 steps and slow moves 1 step
    If fast moves 3 steps, then the intersection might never happen because the decrease is not by 1 here and it won't reach 0 for sure
    '''
    slow = head
    fast = head
    while fast and fast.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt
        if slow == fast:
            return True
    return False

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
print(detectLoop(head))
print(detectLoop(getLinkedList([1, 2, 3, 4, 5, 6])))
print(detectLoop(getLinkedList([1, 2, 3, 4, 5])))
