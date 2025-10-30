# given two positive numbers, return minimum number of bit flips required to convert the start number to the goal number
def minBitFlips(start, goal):
    '''
    Eg: start = 10, goal = 7
    10 - 1 0 1 0
    7  - 0 1 1 1
    we can see that, it requires 3 bits to convert 10 to 7
    we can use xor here to get only the different bits between them
       1 0 1 0
     ^ 0 1 1 1
       -------
       1 1 0 1
    we can see that we got our 3 bits.
    to count them, we can use the technique or checking if ith bit is set or not in the xor result by iterating 0 to 31 since it is an integer
    or we can simply use divide by 2 method to get the bits
    '''
    xor = start ^ goal
    cnt = 0
    for i in range(32):
        if xor & (1 << i):
            cnt += 1
    return cnt

start = 10
goal = 7
print(minBitFlips(start, goal))