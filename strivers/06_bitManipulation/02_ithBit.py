# return if i-th bit set or not for given number
# i starts from 0 at right end and goes till the left end
def isSet(num, i):
    '''
    using left shift and AND operation, we can find
    eg: num = 13, i = 2
    step 1: take 1 and left shift it to i
        1 << 2 = b100
    step 2: do AND num with left shifted 1
        bin(13) = 1101
          1 1 0 1
        & 0 1 0 0
        -------
        0 1 0 0
    since left shift of 1 will result in only the given ith bit set and all other bits as zero,
    doing AND with it will give something greater than 0 only if the ith bit set in the number too.

    using right shift and AND operation too, we can solve it
    step 1:
        right shift the given num to i places, so that the bit we need to check will reach the right most end
        13 >> 2 = b0011
    step 2:
        Do AND right shifted num with 1 and the above mentioned logic applies the same here too
          0 0 1 1
        &       1
          -------
          0 0 0 1
    '''
    return (num & (1 << i)) > 0     # ((num >> i) & 1) > 0

# set the i-th bit in num
def setBit(num, i):
    '''
    We do the same steps as we did above left shift method except
    in step 2, instead of AND, we do OR, so that the ith bit will be set no matter if it is 0 or 1 and all other bits will remain the same as we do OR
    '''
    return (num | (1 << i))

# clear the ith bit in num, i.e, if it's 1, set it to 0. if 0, leave it be.
def clearBit(num, i):
    '''
    step 1: left shift 1 to i places
    step 2: do NOT on the left shifted 1 so that the only existing 1 will turn to 0 and all other 0 bits turn to 1's
    step 3: do AND the negated left shifted 1 with the number
    1 << 2 = b0100
    ~(0100) = 1011
          1 1 0 1  # 13
        & 1 0 1 1  # ~(1 << 2)
          -------
          1 0 0 1  # 9
    '''
    return ~(1 << i) & num

# toggle the ith bit in the num
def toggleBit(num, i):
    '''
    step 1: left shift 1 to i places
    step 2: do XOR num with the left shifted 1
            1 bits at other than ith places will be retained while doing with 0 at respected places, since odd no. of 1's rule
            ith bit will be xor'ed with 1, so if its 1, even no. of 1's rule gives 0 and if its 0, odd no. of 1's rule gives 1
    1 << 2 = b0100
          1 1 0 1   # 13                   1 0 0 1  # 9
        ^ 0 1 0 0   # 1 << 2             ^ 0 1 0 0  # 1 << 2
          -------                          -------
          1 0 0 1   # 9                    1 1 0 1  # 13
    '''
    return (1 << i) ^ num

# clear the last set bin in the num
def clearLastSetBit(num):
    '''
    Lets look a pattern
    num = 16     \|/
        bin(16) = 1 0 0 0 0
        bin(15) = 0 1 1 1 1
    num = 40         \|/
        bin(40) = 1 0 1 0 0 0
        bin(39) = 1 0 0 1 1 1
    num = 84             \|/
        bin(84) = 1 0 1 0 1 0 0
        bin(83) = 1 0 1 0 0 1 1
    From this pattern, we can observe that for a num, num - 1 will have the last set bit of num as 0 and following bits as 1
    if we do AND between num and num - 1, we can achieve our goal
    '''
    return num & (num - 1)

# return if the given num is a power of 2
def isPowerOf2(num):
    '''
    power of 2's = 1, 2, 4, 8, 16, 32, ...
    all these have only the MSB set to 1 and following bits as 0
    so if we do the same step as we did in above clearLastSetBit, we should get 0
    num = 16
        bin(16) = 1 0 0 0 0
        bin(15) = 0 1 1 1 1
                & ---------
                  0 0 0 0 0
    for any number other than power of 2, it won't result as 0
    '''
    return (num & (num - 1)) == 0

def isOdd(num):
    '''
    if we check, the last bit for every odd number will be 1
    and the last bit for every even number is 0
    so, when we do AND of num and 1,
    if it gives 1, it is odd
    if it gives 0, it is even
    num = 2
        1 0
        0 1
      & ---
        0 0
    num = 5
        1 0 1
        0 0 1
      & -----
        0 0 1
    '''
    return num & 1

def divideBy2(num):
    '''
    answer is right shift by 1
    num / 2 = num >> 1
    eg:
    num = 5
        1 0 1
        => (1 * 2 pwr 2) + (0 * 2 pwr 1) + (1 * 2 pwr 0)
        divBy2 => (1 * 2 pwr 1) + (0 * 2 pwr 0)
               => 1 0 = 2
               which is the right shift of 5 by 1
    '''
    return num >> 1

def noOfSetBits(num):
    '''
    There is no one liner solution for this. Only brute force
    but while doing brute force, we can use bit operations
    brute force:
        keep dividing the num by 2 until it becomes 0 and check if its odd which means the current bit is set
        here for dividing by 2 and odd check, we can use the above ways
    '''
    cnt = 0
    while num > 1:
        # if num % 2 == 1:
        #     cnt += 1
        cnt += num & 1
        # num = n // 2
        num = num >> 1
    if num == 1:
        cnt += 1
    return cnt

def noOfSetBits_sol2(num):
    '''
    There is another way to find the no of set bits other than above brute force
    that is using above clear last bit solution
    if we repeat the AND operation step in the solution until the num becomes 0, we can count the set bits
    simply put, for each iteration, we turn off the right most set bit until there are no more set bits
    eg:
    num = 84
        itr1:
            bin(84) = 1 0 1 0 1 0 0
            bin(83) = 1 0 1 0 0 1 1
                    & -------------
            num =     1 0 1 0 0 0 0
        itr2:
            num     = 1 0 1 0 0 0 0
            num - 1 = 1 0 0 1 1 1 1
                    & -------------
            num     = 1 0 0 0 0 0 0
        itr3:
            num     = 1 0 0 0 0 0 0
            num - 1 = 0 1 1 1 1 1 1
                    & -------------
            num     = 0 0 0 0 0 0 0
    '''
    cnt = 0
    while num != 0:
        num = num & (num - 1)
        cnt += 1
