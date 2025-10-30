# given an array of numbers where arr[i] = height of ith bar in histogram
# return the largest rectangle araa that can be formed with the bars
# rectangle - for a i-th bar, a rectangle can be spanned to its left and right with height as its own
# if adjacent bars are equal or greater than itself.
# sample: arr = [2, 1, 5, 6, 2, 3]
# ans is 10 with bars of heights 5 and 6 making rectangle of height 5 i.e., 5 x 2 = 10

from Stack import Stack

def largestRectInHistogram(arr):
    '''
    by looking at the problem, we can say that we should apply nextSmallerElement and prevSmallerElement here
    for i-th bar,
    area = arr[i] x (nse[i] - pse[i] - 1)
    by tracking max of this, we can find our answer.
    but this would take a double traversal first to find pse and then nse to be precomputed and then additional traversal to find our answer
    which would be O(5n)    ->    2n each for pse and nse and another n for finding answer

    our next goal is to optimize it to a single traversal
    lets traverse from left to right there by finding pse in our traversal
    now we need to somehow find nse while doing pse algo

    here is how the pse algo goes
    => for each element, we see if the top of stack is smaller
    => if it is, we push it into stack
    => else we pop until top is smaller or stack is empty and then push it into stack
    => so for every element inside the stack, the immediate down below element is its pse
    => if no element in stack below, then it is the smallest element till now (-1 in our case as we track index)

    here our nse computation comes when we pop from stack
    popping from stack means, the current element is smaller than the top of the stack
    if we reverse our point of view, it can also be interpreted as
    => the current element is the nse of the element at the top of the stack
    now we got nse for the top element
    as for pse, its immediate down below element is its pse
    now we can find our area answer for the top of the stack element

    Eg:
    arr = [3, 2, 10, 11, 5, 10, 6, 3]
    note: stack tracks indices not elements
    i = 0
        ele = 3
        stack is empty, push into stack
        st = [0(3)]
    
    i = 1
        ele = 2
        stack top = 3
            2 < 3
            popping 3   =>  nse(3) = 2
                            pse(3) = none as stack empty below it
                            so for 3 which has i = 0, we can calculate area
                            area = 3 x (1 - (-1) - 1) = 3
                            maxArea = 3
        pushing 2 into stack
        st = [1(2)]
    
    i = 2
        ele = 10
        stack top = 2
            10 > 2
            pushing 10 into stack
        st = [1(2), 2(10)]
        remember we only compute are when we do pop
    
    i = 3
        ele = 11
        stack top = 10
            11 > 10
            pushing 11 into stack
        st = [1(2), 2(10), 3(11)]
    
    i = 4
        ele = 5
        stack top = 11
            5 < 11
            popping 11  =>  nse(11) = 5
                            pse(11) = 10  (next top after 11)
                            area = 11 x (idx(5) - idx(10) - 1)
                                 = 11 x (4 - 2 - 1) = 11
                            maxArea = 11
        st = [1(2), 2(10)]
        stack top = 10
            5 < 10
            popping 10  =>  nse(10) = 5
                            pse(10) = 2
                            area = 10 x (4 - 1 - 1) = 20
                            maxArea = 20
        st = [1(2)]
        stack top = 1
            5 > 2
            pusing 5 into stack
        st = [1(2), 4(5)]
    
    i = 5
        ele = 10
        stack top = 5
            10 > 5
            pushing 10 into stack
        st = [1(2), 4(5), 5(10)]
    
    i = 6
        ele = 6
        stack top = 10
            6 < 10
            popping 10  =>  nse(10) = 6
                            pse(10) = 5
                            area = 10 x (6 - 4 - 1) = 10
                            maxArea = 20
        st = [1(2), 4(5)]
        stack top = 5
            6 > 5
            pushing 6 into stack
        st = [1(2), 4(5), 6(6)]
    
    i = 7
        ele = 3
        stack top = 6
            3 < 6
            popping 6   =>  nse(6) = 3
                            pse(6) = 5
                            area = 6 x (7 - 4 - 1) = 12
                            maxArea = 20
        st = [1(2), 4(5)]
        stack top = 5
            3 < 5
            popping 5   =>  nse(5) = 3
                            pse(5) = 2
                            area = 5 x (7 - 1 - 1) = 25
                            maxArea = 25
        st = [1(2)]
        stack top = 2
            3 > 2
            pushing 3 into stack
        st = [1(2), 7(3)]
    
    All the elements are traversed, but there are still elements in stack. we need to find area for those separately
    for all the remaining elements in the stack, it generally means that there are no nse for them

    top = 3
        nse = none (8 -> len of the arr in our case)
        pse = 2
        area = 3 x (8 - 1 - 1) = 18
        maxArea = 25
        popping 3
        st = [1(2)]
    top = 2
        nse = none
        pse = none (-1 in our case)
        area = 2 x (8 - (-1) - 1) = 16
        maxArea = 25
    '''
    n = len(arr)
    st = Stack()
    maxArea = 0
    for i in range(n):
        while not st.isEmpty() and arr[st.top()] > arr[i]:
            idx = st.pop()
            nse = i
            pse = -1 if st.isEmpty() else st.top()
            area = arr[idx] * (nse - pse - 1)
            maxArea = max(area, maxArea)
        st.push(i)
    while not st.isEmpty():
        idx = st.pop()
        nse = n
        pse = -1 if st.isEmpty() else st.top()
        area = arr[idx] * (nse - pse - 1)
        maxArea = max(area, maxArea)
    return maxArea

arr = [3, 2, 10, 11, 5, 10, 6, 3]
print(largestRectInHistogram(arr))