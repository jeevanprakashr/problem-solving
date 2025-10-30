# given an array of nums, where each element repeats twice except a single number. Find that single number
def singleNumber(nums):
    '''
    brute force is to use map
    instead we can use xor here by keep xoring each element in the array, so that a number can cancel itself if it repeats and only the single number remains
    '''
    xor = 0
    for num in nums:
        xor = xor ^ num
    return xor

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))