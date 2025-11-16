# given an array of numbers and k, return no. of subarrays with exactly k distinct numbers in them

def noOfSubArrsWKDiffNums(arr, k):
    '''
    if we follow the sliding window solution straight away we saw in previous problems, we will have a problem.

    Lets see with this example,
    arr = [2, 1, 1, 1, 3, 4, 3, 2]  k = 3

    lets have
    l and r at
    [2, 1, 1, 1, 3, 4, 3, 2]
        l           r
    
    now this is a satisfying subarray
    so we increment out result counter

    now according to sliding window pattern, our next step would be increment r
    [2, 1, 1, 1, 3, 4, 3, 2]
        l              r
    now this is also a valid window, but by doing this, we miss out on
    [2, 1, 1, 1, 3, 4, 3, 2]
           l        r
              l     r
    this two valid windows.

    now this is the problem that we face. Not able to decide whether to shrink or expand the window
    
    to solve this type of problem, we are gonna use the same solution we did in 05_binarySubArrsWithKSum and 06_noOfKOddNumsSubArrs
    we need to modify our goal to finding no. of subarrays with distinct nums <= k
    for this problem, our sliding window approach would work

    once we can find this, then our actual solution is
    subarrs <= k    -   subarrs <= k - 1
    '''
    def noOfSubArrsWLTEKDiffNums(arr, k):
        # constaint: k >= 1
        n = len(arr)
        mpp = dict()
        l = 0
        r = 0
        cnt = 0
        while r < n:
            mpp[arr[r]] = mpp.get(arr[r], 0) + 1
            while len(mpp) > k:
                mpp[arr[l]] -= 1
                if mpp[arr[l]] == 0:
                    mpp.pop(arr[l])
                l += 1
            cnt += r - l + 1
            r += 1
        return cnt
    return noOfSubArrsWLTEKDiffNums(arr, k) - noOfSubArrsWLTEKDiffNums(arr, k - 1)

arr = [2, 1, 1, 1, 3, 4, 3, 2]
k = 3
print(noOfSubArrsWKDiffNums(arr, k))
