# given an array of integers, return sum of all subsets of the array in increasing order
# Eg: arr = [3, 1, 2] ans = [0, 1, 2, 3, 3, 4, 5, 6]   no of subsets = 2 ^ n

def accumulateSubsetSums(idx, arr, sm, res):
    if idx == len(arr):
        res.append(sm)
        return
    accumulateSubsetSums(idx + 1, arr, sm + arr[idx], res)
    accumulateSubsetSums(idx + 1, arr, sm, res)

def subsetSum(arr):
    '''
    Brute force is to generate all subset of the array using power set method (bit manipulation method)
    Optimal approach would be pick and not pick method
    '''
    res = []
    accumulateSubsetSums(0, arr, 0, res)
    res.sort()
    return res

arr = [3, 1, 2]
print(subsetSum(arr))