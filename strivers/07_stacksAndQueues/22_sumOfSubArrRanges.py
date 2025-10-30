# given an array of numbers, return the sum of the ranges of all possible subarrays
# range - difference between largest and smallest number in an array
from Stack import Stack

def sumOfSubArrRanges(arr):
    '''
    To solve this, refer sumOfSubArrMins code
    We use the same we used there to find both sumOfSubArrMins and subOfSubArrMaxs
    ans our res is (subOfSubArrMaxs - sumOfSubArrMins)
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
    
    def getNGE(arr):
        n = len(arr)
        st = Stack()
        nge = [n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            while not st.isEmpty() and arr[st.top()] <= arr[i]:
                st.pop()
            nge[i] = n if st.isEmpty() else st.top()
            st.push(i)
        return nge
    
    def getPGEE(arr):
        n = len(arr)
        st = Stack()
        pgee = [-1 for _ in range(n)]
        for i in range(n):
            while not st.isEmpty() and arr[st.top()] < arr[i]:
                st.pop()
            pgee[i] = -1 if st.isEmpty() else st.top()
            st.push(i)
        return pgee
    
    n = len(arr)
    nse = getNSE(arr)
    psee = getPSEE(arr)
    nge = getNGE(arr)
    pgee = getPGEE(arr)
    sumOfSubArrMins = 0
    sumOfSubArrMaxs = 0
    for i in range(n):
        left = i - psee[i]
        right = nse[i] - i
        sumOfSubArrMins += left * right * arr[i]  # mod 1e9 + 7
        left = i - pgee[i]
        right = nge[i] - i
        sumOfSubArrMaxs += left * right * arr[i]
    return sumOfSubArrMaxs - sumOfSubArrMins

arr = [1, 4, 3, 2]
print(sumOfSubArrRanges(arr))
