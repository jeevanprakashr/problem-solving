# similar to the previous question, but the array is a circular one,
# i.e., if there is no greater element to the right, consider the array end connects with with start
# and start looking from the start of the array. If still no greater element found, put -1

from Stack import Stack

def nextGreaterElement2(arr):
    '''
    Here, we hypothetically double the arr like
    [2, 10, 12, 1, 11]  ->   [2, 10, 12, 1, 11, 2, 10, 12, 1, 11]
    the second part is just considered via index by using i % n where i = 0 to 2n - 1
    now do the same as we did before, but only store elements in nge for the first part, i.e. i = 0 to n - 1
    for the second part, only update the monotonic stack
    '''
    n = len(arr)
    nge = [-1 for i in range(n)]
    st = Stack()
    end = (2 * n) - 1
    for i in range(end, -1, -1):
        idx = i % n
        while not st.isEmpty() and st.top() <= arr[idx]:
            st.pop()
        if i < n:
            if st.isEmpty():
                nge[i] = -1
            else:
                nge[i] = st.top()
        st.push(arr[idx])
    return nge

arr = [2, 10, 12, 1, 11]
print(nextGreaterElement2(arr))