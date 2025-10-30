# given an array of elements arr, return an array res in which res[i] contains the nearest greater element to the right of arr[i] in arr

from Stack import Stack

def nextGreaterElement(arr):
    '''
    The brute force approach would be for each element at i, traverse from i + 1 to n - 1 and find the nearest greater element
    Optimal approach:
    We use something called Monotonic Stack
    Monotonic Stack:
        The elements are stored in the stack in such a way that, they follow a strict order like either increasing or decreasing.
        If any new element needs to be pushed to stack and it violates this order, pop elements from stack until it satisfies.
    Steps:
    Start from the end of the array
    the NGE of the element is the top of the stack if top > element, else pop until it satisfies
    if stack is empty, then NGE is -1
    then push the element to stack
    but check if the top of the stack is greater than the element and then push it
    if not, pop until it satisfies the condition or stack is empty and then push it

    this is otherwise known as lightpole concept
    from pov of observer, lightpole are arranged in the same line and which farthest lightpole can be seen by the observer?
    '''
    n = len(arr)
    nge = [-1 for i in range(n)]
    st = Stack()
    for i in range(n - 1, -1, -1):
        while not st.isEmpty() and st.top() <= arr[i]:
            st.pop()
        if st.isEmpty():
            nge[i] = -1
        else:
            nge[i] = st.top()
        st.push(arr[i])
    return nge

arr = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
print(nextGreaterElement(arr))