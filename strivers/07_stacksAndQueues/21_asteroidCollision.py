# given an array of numbers where
# arr[i] - weight of asteroid
# positive - asteroid moves forward
# negative - asteroid moves backward
# when asteroids next to each other moving opposite direction, they colloide and
# asteroid with smaller absolute weight value gets destroyed and 
# asteroid with larger weight remains
# if both are equal, both get destoyed
# after all collisions completed, return the final array
'''
Sample:
arr = [4, 7, 1, 1, 2, -3, -7, 17, 15, -16]
asteroids from i = 0 to i = 4 all moves forward
i = 5:
    weight = -3, moves backward
    [2, -3]  -  2 is smaller and gets destroyed
    [1, -3]  -  1 is smaller and gets destroyed
    [1, -3]  -  1 is smaller and gets destroyed
    [7, -3]  -  3 is smaller and gets destroyed
    so res = [4, 7, -7, 17, 15, -16]
i = 6:
    weight = -7, moves backward
    [7, -7]  -  both equal, both get destroyed
    so res = [4, 17, 15, -16]
i = 7:
    weight = 17, moves forward
    so res = [4, 17, 15, -16]
i = 8:
    weight = 15, moves forward
    so res = [4, 17, 15, -16]
i = 9:
    weight = -16, moves backward
    [15, -16]  -  15 is smaller and gets destroyed
    [17, -16]  -  16 is smaller and gets destroyed
    so res = [4, 17]
the final answer is [4, 17]
'''

from Stack import Stack

def asteroidCollision(arr):
    '''
    From the sample itself, we can know that we should use stack in this case
    - If a +ve weight encountered, push it into stack
    - If a -ve weight encountered, compare it with the top of stack
        - If top is greater, move on to next asteroid
        - else pop until top is greater and move on to next asteroid
        - If stack is empty, push the -ve asteroid into stack, as we need it in the result
        - If top is also -ve, push into stack
    return the elements in the stack as in the same order as inserted.
    '''
    st = Stack()
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            st.push(arr[i])
        else:
            while not st.isEmpty() and st.top() > 0 and st.top() < abs(arr[i]):
                st.pop()
            if not st.isEmpty() and st.top() == abs(arr[i]):
                st.pop()
            elif st.isEmpty() or st.top() < 0:
                st.push(arr[i])
    return st.stack

arr = [4, 7, 1, 1, 2, -3, -7, 17, 15, -16]
arr = [4, 7, 1, 1, 2, -3, -7, 17, 15, -18, -19]
print(asteroidCollision(arr))
