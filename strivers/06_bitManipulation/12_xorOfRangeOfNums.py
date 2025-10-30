# given an integer n, find the xor of all numbers from 1 to n.
def xorOfRangeOfNums1(n):
    '''
    brute force is running a for loop and keep xoring from 1 to n
    efficient approach is to know the pattern first
    n = 1   1   =>  1
    n = 2   3   =>  1 ^ 2
    n = 3   0   =>  1 ^ 2 ^ 3
    n = 4   4   =>  1 ^ 2 ^ 3 ^ 4

    n = 5   1
    n = 6   7
    n = 7   0
    n = 8   8

    n = 9   1
    ...

    if we look at this, we can see a pattern that the numbers can be split into block of 4
    n % 4 == 1  =>  1
    n % 4 == 2  =>  n + 1
    n % 4 == 3  =>  0
    n % 4 == 0  =>  n
    '''
    mod = n % 4
    if mod == 1:
        return 1
    if mod == 2:
        return n + 1
    if mod == 3:
        return 0
    return n

# find the xor of numbers between given two numbers l and r
def xorOfRangeOfNums2(l, r):
    '''
    we can use the above method to solve this too in O(1)
    first, we find xor of 1 to l - 1
    then, we find xor of 1 to r
    then if we xor them two answers, we get our result
    Eg: l = 4, r = 7
    xor(1-3) = 1 ^ 2 ^ 3
    xor(1-7) = 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7
    if we xor these two, according to how xor works, 1 and 1 will cancel each other
    2 and 2 will cancel each other
    3 and 3 will cancel each other
    at last only 4 ^ 5 ^ 6 ^ 7 will remain which is our answer
    '''
    lxor = xorOfRangeOfNums1(l - 1)
    rxor = xorOfRangeOfNums1(r)
    return lxor ^ rxor

print(xorOfRangeOfNums1(7))
print(xorOfRangeOfNums2(4, 7))
