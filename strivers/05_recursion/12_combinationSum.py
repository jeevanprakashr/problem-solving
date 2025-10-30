# given an arr and target, return all unique combinations whose sum is target. A num can be chosen multiple times
# arr = [2, 3, 6, 7]    target = 7
# res = [[2, 2, 3], [7]]

def findCombination(idx, arr, target, comb, resCombs):
    '''
    idx - current index where we should either pick or not pick the element
    arr - array of elements
    target - target to reach yet. goal is to make it 0 by picking elements and subtracting them from it.
    comb - picked elements so far
    resCombs - result array of satisfied combinations
    '''
    if idx == len(arr):
        if target == 0:
            resCombs.append(list(comb))
        return
    # can use below commented code too to reduce recursion calls
    # if target == 0:
    #     resCombs.append(list(comb))
    #     return
    # if idx == len(arr):
    #     return
    if arr[idx] <= target:
        comb.append(arr[idx])
        findCombination(idx, arr, target - arr[idx], comb, resCombs)
        comb.pop()
    findCombination(idx + 1, arr, target, comb, resCombs)

    
def combinationSum(candidates, target):
    '''
    At each index, we have two options
    1. pick
    2. not pick

    when pick, stay at the same index after picking the element for our combination since we can choose multiple times
    when not pick, move to the next index (before moving, remove the element that we picked for our pick option before)
    '''
    comb = []
    resCombs = []
    findCombination(0, candidates, target, comb, resCombs)
    return resCombs

arr = [2, 3, 6, 7]
target = 7
print(combinationSum(arr, target))