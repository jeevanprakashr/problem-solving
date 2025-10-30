# given an array, return all the subsets or power set of it
# power set is when solved using bit manipulation
def powerSet(arr):
    '''
    no. of subset of an n-length arr is 2^n
    n = 1 => nos = 2
    n = 2 => nos = 4
    n = 3 => nos = 8
    n = 4 => nos = 16
    => 2^n  or  1 << n
    Eg: nums = [1, 2, 3]
    we have n = 3
    nums   [3  2  1]
    idx     2  1  0
            -------
            0  0  0     []
            0  0  1     [1]
            0  1  0     [2]
            0  1  1     [1  2]
            1  0  0     [3]
            1  0  1     [1  3]
            1  1  0     [2  3]
            1  1  1     [1  2  3]
    for each subset bits, we collect all the set bits in it and get the corresponding index element in the nums and add it to the subset
    '''
    n = len(arr)
    res = []
    nos = 1 << n
    for i in range(nos):
        subset = []
        for j in range(n):
            setBit = 1 << j
            if i & setBit:
                subset.append(nums[j])
        res.append(subset)
    return res

nums = [1, 2, 3]
print(powerSet(nums))