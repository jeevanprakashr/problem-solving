from LinkedList import Node, printLinkedList, getLinkedList

# return the starting point of the loop in the linked list if any exist or return none

def startingPointOfLoop(head):
    '''
    Gonna use same tortoise and hare method as we did in previous problem
    Step 1:
        Detect the existance of loop using tortoise and hare method. If doesn't exist, return none
    Step 2:
        Revert one of the slow and fast pointer back to head and keep the other one at the intersection node itself.
        Now move both the pointers by 1 step forward in each iteration.
        When they intersect again, that is the starting point of the loop
    
    Intuition:
    Our thought process starts the moment the slow pointer reaches the starting point of a loop.
    When slow is at start of loop,
        distance from head to slow/loopStart = L1
    which makes
        distance from head to fast = 2 * L1  (as fast jumps 2 steps)
        distance from slow/loopStart to fast = L1
    lets say
        distance from fast to slow/loopStart = d  (as inside loop)
    so we can say
        length of loop = (loopStart to fast) + (fast to loopStart)
                       = L1 + d
    
    Due to the fact that d decreases in each iteration by 1 and eventually becomes 0 when slow and fast intersects,
    it would take d iterations from the "slow at start of loop" moment to intersect
    so in that d iterations
        distance covered by fast = 2d       (fast jumps by 2 steps for 1 iteration, so for d iterations, 2d)
        distance covered by slow = d
    
    Now that we are at intersection point where both slow and fast pointers are currently at,
        distance from loopStart to intersection = d     (distance covered by slow from loopStart)
    which tells us that
        distance from intersection to loopStart = L1    (length of loop = L1 + d)
    
    Remember,
        distance from head to loopStart = L1
    So, if we move slow back to head and make them jump 1 step for each iteration, they would intersect again at loopStart
    as fast moves from intersection to loopStart
    and slow moves from head to loopStart and both distances are L1
    '''
    slow = head
    fast = head
    while fast and fast.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.nxt
                fast = fast.nxt
            return slow
    return None

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
print(startingPointOfLoop(head))
print(startingPointOfLoop(getLinkedList([1, 2, 3, 4, 5])))