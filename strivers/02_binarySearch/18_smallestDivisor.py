# given an array and threshold, find the smallest divisor such that sum of "ceiled" quotient is lesser than threshold
'''
Eg: [1, 2, 5, 9]
div = 4
[1/4, 2/4, 5/4, 9/4] = [1, 1, 2, 3]  (ceil)
= 7 > 6
so 4 is not answer

div = 5
=> [1, 1, 1, 2]
= 5 <= 6
5 is the answer
if 5 is an answer, then anything above 5 like 6, 7, 8,... are all answers
5 is the smallest one hence 5 is the answer

question is asking for positive divisor
'''

def smallestDivisorGivenT(arr, t):
    '''
    minimum quotient we can get for an element is 1
    to get minimum quotient sum (which is length of arr), minimum divisor should be max of arr
    so max of arr will be our high of BS
    '''
    def possible(divisor):
        sm = 0
        for i in range(n):
            sm += arr[i] // divisor
            # need ceil here
            if arr[i] % divisor != 0:
                sm += 1
        return sm <= t
    
    n = len(arr)
    if n > t:
        return -1
    low = 1
    high = max(arr)
    while low <= high:
        mid = low + ((high - low) // 2)
        if possible(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [1, 2, 5, 9]
t = 7
# t = 3
print(smallestDivisorGivenT(arr, t))