# given an array of numbers, return the sum of the minimums of all the possible subarrays
# Eg: [3, 1, 2, 4]
# subArr starting with 3 -> [3], [3, 1], [3, 1, 2], [3, 1, 2, 4] -> minimums of these subArrs = 3, 1, 1, 1 -> sum = 6
# similarly we do for all possible sub arrays and return the total of all the sub array minimums
# ans = 17
# if ans is too large to be stored, mod with 10^9 + 7 and return

from Stack import Stack

def sumOfSubArrMins(arr):
    '''
    Lets take the example
    arr = [3, 1, 2, 4]
    [3]             -   3
    [3, 1]          -   1
    [3, 1, 2]       -   1
    [3, 1, 2, 4]    -   1
    [1]             -   1
    [1, 2]          -   1
    [1, 2, 4]       -   1
    [2]             -   2
    [2, 4]          -   2
    [4]             -   4
    Total is 17

    the brute force would be generating all subarrays and it would take O(n2)
    Instead, let's try to find how many times each element is contributed as the smallest number of a subarray
    3   -   1x
    1   -   6x
    2   -   2x
    4   -   1x
    => (1x3) + (6x1) + (2x2) + (1x4) = 17
    we got our answer

    How to find the no. of contributions of each element:
    Lets take another example
    arr = [1, 4, 6, 7, 3, 7, 8, 1]

    Lets try to find no. of contributions of 3
    3 would be minimum as long as first and last 1 don't enter as part of the subarray
    so on the left, 3 can form 4 subarrays
    on the right, 3 can form 3 subarrays
    both combined, 3 can form 4x3=12 subarrays
    so no. of contributions of 3 = 12x
    => 12x3 = 36
    If we keep on adding the no. of contributions for every element, we get our answer

    How to find no. of subarrays to the left and right:
    For this we use NextSmallerElement and PrefixSmallerElement method, but this time, we record index instead of the element itself
    NSE(3) = 1
    Idx(NGE(3)) =  7
    Idx(3)  =   4
    => right sub arrays = 7 - 4 = 3

    PSE(3) = 1
    Idx(PSE(3)) =  0
    Idx(3) = 4
    => left sub arrays = 4 - 0 = 4

    If there are no smaller elements on right or left, consider it as
    right Idx = n
    left Idx = -1
    so that we can take all the elements on right or left

    There is one edge case here
    consider arr = [1, 1]
    for this
    nse = [2, 2]
    pse = [-1, -1]
    remember nse and pse are indices

    i = 0:
        right sub arrs = 2-0 = 2  =>  [1], [1, 1]
        left sub arrs = 0-(-1) = 1   =>  [1]
        so 2x1 = 2
    i = 1
        right sub arrs = 2-1 = 1    =>  [1]
        left sub arrs = 1-(-1) = 2  =>  [1, 1]
        so 2x1 = 2
    here we are considering [1, 1] twice for both the elements, which is wrong.
    so, we should either consider it for first element or the last element
    so instead of doing NSE and PSE
    we should do either NextSmallerElement and PrefixSmallerOrEqualElement
    or NextSmallerOrEqualElement and PrefixSmallerElement

    If we follow NextSmallerElement and PrefixSmallerOrEqualElement
    nse = [2, 2]
    psee = [-1, 0] => 0 as a result of 'OrEqual'

    i = 1
        right = 2-1 = 1
        left = 1-0 = 1
        => 1x1 = 1
    we get our expected result as 3
    '''
    def getNSE(arr):
        n = len(arr)
        st = Stack()
        nse = [n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            # Don't confuse '>=' here with psee
            # we pop for stack even if the top is equal which means we are not consider "equals" (as noun) as next smaller element
            while not st.isEmpty() and arr[st.top()] >= arr[i]:
                st.pop()
            nse[i] = n if st.isEmpty() else st.top()
            st.push(i)
        return nse
    
    def getPSEE(arr):
        n = len(arr)
        st = Stack()
        psee = [-1 for _ in range(n)]
        for i in range(n):
            # here we only pop if top is greater and don't pop if top is equal
            # which means we do consider "equals" (as noun) as we need prefix smaller or equal element
            while not st.isEmpty() and arr[st.top()] > arr[i]:
                st.pop()
            psee[i] = -1 if st.isEmpty() else st.top()
            st.push(i)
        return psee
    
    n = len(arr)
    total = 0
    nse = getNSE(arr)
    psee = getPSEE(arr)
    for i in range(n):
        left = i - psee[i]
        right = nse[i] - i
        total += left * right * arr[i]  # mod 1e9 + 7
    return total

arr = [3, 1, 2, 4]
arr = [1, 4, 6, 7, 3, 7, 8, 1]
print(sumOfSubArrMins(arr))
