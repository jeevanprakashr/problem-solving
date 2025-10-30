# given 2 linked list, return the first node where two lists join one another, if none return none
from LinkedList import Node, printLinkedList, getLinkedList

def findIntesectionNode(head1, head2):
    '''
    We can find the intersection point, if we somehow synchronize the pointers of 2 lists to start at same length
    Eg:
                    3 -> 1
                          \_> 4 -> 6 -> 2 -> x
                          /
        1 -> 2 -> 4 -> 5 -
    If we somehow make the traverse to start from 3 for l1 and 4 from l2, we can make them to colloide and get our result
    We can achive that by swapping the pointers to heads of opposite lists when the current list is exhausted
    Reason:
    The diff in length between the shorter and larger lists is 2 which can be d
    that means, the short pointer will reach the end first and the large pointer will be 2 steps behind
    once the short pointer reaches the end, we shift it back to the head of the larger list
    now when we commence the traversing, when the large pointer reaches the end, the short pointer will also be tranversed d steps
    if we swap the large pointer back to the head of short list now, the pointers would have been synchronized.
    '''
    if not head1 or not head2:
        return None
    t1 = head1
    t2 = head2
    while t1 != t2: # if both are same lists
        t1 = t1.nxt
        t2 = t2.nxt
        if t1 == t2:
            return t1  # works for not intersecting lists too, as both of them would be None here after completing the traversing
        if not t1:
            t1 = head2
        if not t2:
            t2 = head1
    return t1 # if both are same lists

head1 = getLinkedList([3, 1, 4, 6, 2])
head2 = getLinkedList([1, 2, 4, 5])
temp = head2
while temp.nxt:
    temp = temp.nxt
temp.nxt = head1.nxt.nxt
printLinkedList(head1)
print()
printLinkedList(head2)
y = findIntesectionNode(head1, head2)
print()
print(y)