# given an array of numbers where each number occurs twice except two distinct numbers, return those two numbers in any order
def singleNumber3(nums):
    '''
    we solve this using concept of buckets
    lets take an example
    nums = [2, 4, 2, 14, 8, 7, 7, 8]
    First, we do xor on all the elements in the nums array.
    So every element that occurs twice will cancel each other and we remain with xor of our two distinct elements
    Since these are two distinct numbers, we know for the fact that there will be atleast one bit which is different between them
    and those distinct bit positions can be found from the final result of xor
    in our case, we got 4 ^ 14 = 10 = b1010
    from it we choose any one distinct bit position, and we split the nums into two buckets based on that bit position

    lets take 1st bit position and have two buckets
    b1 = nums with 1st bit set
    b2 = nums with 1st bit not set
    we would get
    b1 = [2, 2, 14, 7, 7]
    b2 = [4, 8, 8]
    
    if we do xor on these two buckets, we would get our two distinct numbers
    b1 = 14
    b2 = 4

    to choose a set bit, we choose the right most set bit and to find it, we use
    (num & (num - 1)) ^ num
    
    we know n & (n - 1) will flip all the right most set bit in n from 02_ithBit.clearLastSetBit
    so, 1 0 1 0  -->  1 0 0 0
    no if we do xor between these two, we would get the right most set bit
      1 0 1 0
      1 0 0 0
    ^ -------
      0 0 1 0
    '''
    xor = 0
    for num in nums:
        xor = xor ^ num
    rightMostSetBit = (xor & (xor - 1)) ^ xor       # in other languages, use xor as long as xor - 1 would overflow if xor = -2 pwr 31
    b1 = 0
    b2 = 0
    for num in nums:
        if num & rightMostSetBit:
            b1 = b1 ^ num
        else:
            b2 = b2 ^ num
    return [b1, b2]

arr = [2, 4, 2, 14, 8, 7, 7, 8]
print(singleNumber3(arr))