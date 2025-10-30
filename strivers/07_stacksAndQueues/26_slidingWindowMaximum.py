# given an array of both positive and negative numbers and a number k
# return: array of maximums of all sliding windows of length k
# sample: arr = [1, 3, -1, -3, 5, 3, 2, 1, 6]   k = 3
# window        max
# [1, 3, -1]    3
# [3, -1, -3]   3
# [-1, -3, 5]   5
# [-3, 5, 3]    5
# [5, 3, 2]     5
# [3, 2, 1]     3
# [2, 1, 6]     6
# ans = [3, 3, 5, 5, 5, 3, 6]

from Deque import Deque

def slidingWindowMaximum(arr, k):
    '''
    Since this is a sliding window, we need a data structure where we can add from one end and pop from another end
    And also we need to track the maximum while popping out
    The first one looks like a queue application and the second looks like monotonic stack application
    So we use Deque which can be pushed and popped from both ends for our solution
    
    our monotonic stack is decreasing stack (pyramid shape) - we need max element at the bottom of the stack

    here are the steps (we store index in our deque):
    1. if queue's front (stack's bottom) has an index beyond the window size (index before i), pop it out
    2. pop from stack (popBack from queue) until top-th is greater than i-th element or stack/queue is empty
    3. push i into stack (pushBack into queue)
    4. if i went k-1, i.e. sliding window can be formed, add queue's front -th element (stack's bottom) to our result array
    '''
    n = len(arr)
    dq = Deque()
    res = []
    for i in range(n):
        if not dq.isEmpty() and dq.topFront() <= i - k:
            dq.popFront()
        while not dq.isEmpty() and arr[dq.topBack()] <= arr[i]:
            dq.popBack()
        dq.pushBack(i)
        if i >= k - 1:
            res.append(arr[dq.topFront()])
    return res

arr = [1, 3, -1, -3, 5, 3, 2, 1, 6]
arr = [1, 3, -1, -3, 5, 3, 7, 1, 6]
k = 3
print(slidingWindowMaximum(arr, k))