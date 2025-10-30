# given an arr of numbers where each number repeats itself thrice except one number, return that single number

def singleNumber2(arr):
    '''
    Lets take an example
    arr = [5, 5, 4, 6, 4, 5, 4]
    5   -   1 0 1
    5   -   1 0 1
    4   -   1 0 0
    6   -   1 1 0
    4   -   1 0 0
    5   -   1 0 1
    4   -   1 0 0
    since it is said that a number appears 3 times,
    we can say that the no. of bits set at each i-th position for all numbers is a multiple of three.
    If it is not a multiple of three, then the bit at that particular position is set for our single number

    Let's take 0th bit:
        we have 3 numbers with bit set at 0th bit
        so our single number doesn't have a set bit at 0th position
        ans = _ _ 0
    1st bit:
        no. of set bits at 1st pos = 1
        1 % 3 != 0
        so our single number have a set bit at 1st position
        ans = _ 1 0
    2nd bit:
        no.of set bits at 2nd pos = 7
        7 % 3 != 0
        so our single number have a set bit at 2nd position
        ans = 1 1 0
    
    like this we can go on checking for 0 to 31 positions for integer
    TC: O(n * 32)
    '''
    ans = 0
    for bitPos in range(32):
        cnt = 0
        for num in arr:
            if num & (1 << bitPos):
                cnt += 1
        if cnt % 3 != 0:
            ans = ans | (1 << bitPos)
    return ans

def singleNumber2_better(arr):
    '''
    Another way is to sort the arr.
    since the array is sorted and we know the repeated elements will be in group of 3,
    we can iterate through every middle element of each group and check with previous element if they are equal.
    since there is a single number among them, at some point, that number will break this pattern and we can find it.
    this covers if that number is at the beginning or at the middle. if it is at the end, then we simple return the last number if the loop exhausts.
    TC: O(n log n) + O(n / 3)
    '''
    arr.sort()
    i = 1
    n = len(arr)
    while i < n:
        if arr[i] != arr[i - 1]:
            return arr[i - 1]
        i += 3
    return arr[n - 1]

def singleNumber2_optimal(arr):
    '''
    Eg: [2, 2, 2, 1]
    we are going to use something called concept of buckets
    we create two buckets/variables
    ones and twos (we can also create threes since nums are appearing thrice, but threes won't be of any use)
    1. nums[i] will go into ones if it is not in twos
    2. nums[i] will go into twos if it is in ones
    3. nums[i] will go into threes if it in twos
    for each num in arr, we try to push the num to ones and twos, so that the above conditions satisfy
    intially ones = 0 and twos = 0
    we simply pick the num from previous bucket and put it to the next bucket if the num already exists in the previous bucket
    so the formula is
    ones = (ones ^ arr[i]) & ~twos          # xor is for trying to add to the ones bucket and neg is for checking twos bucket dosn't already has the number
    twos = (twos ^ arr[i]) & ~ones          # so to put simply, if xor AND neg passes, add the number to the bucket
    i = 0, num = 2
        ones = 0    =>  ones = (0 ^ 2) & ~0  =  2 & 1  =  2
        twos = 0    =>  twos = (0 ^ 2) & ~2  =  2 & ~2  =  0
    i = 1, num = 2
        ones = 2    =>  ones = (2 ^ 2) & ~0  =  0 & 1  =  0
        twos = 0    =>  twos = (0 ^ 2) & ~0  =  2 & 1  =  2
    i = 2, num = 2
        ones = 0    =>  ones = (0 ^ 2) & ~2  =  2 & ~2  =  0
        twos = 2    =>  twos = (2 ^ 2) & ~0  =  0 & 1  =  0
    i = 3, num = 1
        ones = 0    =>  ones = (0 ^ 1) & ~0  =  1 & 1  =  1
        twos = 0    =>  twos = (0 ^ 1) & ~1  =  1 & 0  =  0
    
    the answer will be ones. the order of nums doesn't matter. the bits will take care of it
    TC: O(n)
    '''
    ones = 0
    twos = 0
    for num in arr:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones


arr = [5, 5, 4, 6, 4, 5, 4]
print(singleNumber2(arr))
print(singleNumber2_better(arr))
print(singleNumber2_optimal(arr))