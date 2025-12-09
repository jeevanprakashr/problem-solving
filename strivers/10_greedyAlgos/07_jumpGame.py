# given an array of numbers
# each position in the array represents a stair
# the number at a position represents maximum no. of steps one can take from that position skipping those steps
# return if it is possible or not to reach the last step
# sample:
# arr = [2, 3, 1, 0, 4]
# res = possible 2 -> 3 -> 4
# arr = [3, 2, 1, 0, 4]
# res = not possible - whatever way we took, we would get locked at the 4th step with 0

def jumpGame(arr):
    '''
    from the sample, one thing is clear.
    If there is no zero in the arr, we can definitely reach the end.
    Now lets solve with an array that has 0.

    eg: arr = [1, 2, 3, 1, 1, 0, 2, 5]
    indices = 0 to 7
    idx     steps       possible can be reached idxs
    0       1           1
    1       2           2, 3
    2       3           3, 4, 5
    3       1           4
    4       1           5
    5       0           -
    6       2           wait, for the above possible reachable steps, there is no index 6
                        so there is no way one can reach the index 6
                        so the answer is not possible
    
    this is our thought process
    we can see that we track for each step if that particular step can be reached from anywhere.
    so for each step we track the maximum index one can reach and we keep updating the maxIndex for each index
    if we are at an index which is greater than the maxIndex we've tracked so far, then we can say that this index can't
    be reached from anywhere.
    The greedy approach here is that we always keep trying to reach the farthest index and we keep on maximizing it until we reach the end.
    '''
    n = len(arr)
    maxIdx = 0
    for i in range(n):
        if i > maxIdx:
            return False
        maxIdx = max(maxIdx, i + arr[i])
        # we can optimize it by adding a if condition here to check whether we have reached the end.
    return True

arr = [1, 2, 3, 1, 1, 0, 2, 5]
arr = [1, 2, 4, 1, 1, 0, 2, 5]
print(jumpGame(arr))