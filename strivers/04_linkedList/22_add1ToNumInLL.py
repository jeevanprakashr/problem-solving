# given a linked list representing a number, add 1 to that number and return the new linked list
from LinkedList import Node, printLinkedList, getLinkedList

class Add1ToNumInLL:
    '''
    There are two approaches for this solution
    Approach 1:
        1. Reverse the LL
        2. Add 1 from new head and traverse
        3. Reverse it back
        4. If there is still a carry, create a new node with 1 and add before the head and return the new node
    Approach 2:
        Use recursion and add 1 while backtracking
        Base case: if no node, return 1 as carry
        add the returned carry to the curr node and backtrack
        when there is carry returned after the complete recursion, add a new node as 1 before the head and return it
    '''
    def iterative(self, head):
        def reverse(head):
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
        
        head = reverse(head)
        temp = head
        carry = 1
        while temp:
            temp.data += carry
            if temp.data < 10:
                carry = 0
                break
            temp.data = 0
            carry = 1
            temp = temp.nxt
        head = reverse(head)
        if carry:
            node = Node(1, head)
            return node
        return head
    
    def recursion(self, head):
        def helper(temp):
            if not temp:
                return 1
            carry = helper(temp.nxt)
            temp.data += carry
            if temp.data < 10:
                return 0
            temp.data = 0
            return 1
        
        carry = helper(head)
        if carry:
            node = Node(1, head)
            return node
        return head
    

head = getLinkedList([1, 5, 9])
head = getLinkedList([9, 9, 9, 9])
sol = Add1ToNumInLL()
head = sol.recursion(head)
printLinkedList(head)