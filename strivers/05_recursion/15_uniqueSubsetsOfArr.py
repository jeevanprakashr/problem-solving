# given an array, return all the possible subsets in any order, and the subset itself can have nums in any order
# but the subset should be unique i.e., there should be only one copy of a sorted subset
# [1, 2, 2] and [1, 2, 1] are the same

def generateUniqueSubsets(idx, nums, ds, res):
    res.append(list(ds))
    for i in range(idx, len(nums)):
        if i != idx and nums[i] == nums[i - 1]:
            continue
        ds.append(nums[i])
        generateUniqueSubsets(i + 1, nums, ds, res)
        ds.pop()

def uniqueSubsets(nums):
    '''
    We are going to use the same pattern we did in 13_combinationSum2 to generate unique subsets
    '''
    nums.sort()
    res = []
    generateUniqueSubsets(0, nums, [], res)
    return res

nums = [1, 2, 2, 2, 3, 3]
print(uniqueSubsets(nums))