# given an arr and target, return all unique combinations whose sum is target. A num can be chosen only once
# and there should not be duplicate combinations so return combination as sorted.
# duplicate combinations means elements at different indices in the array are considered same element if they are equal
# arr = [1, 1, 1, 2, 2]    target = 4
# [1, 1, 2] , [2, 1, 1] , [1, 2, 1] are all considered as duplicates even though '1' can be any element among the three '1's
# res = [[1, 1, 2], [2, 2]]

def findCombinations(idx, arr, target, comb, resCombs):
    '''
    idx - starting index of the array for picking an element till the last element of the array
    '''
    if target == 0:
        resCombs.append(list(comb))
        return
    if idx == len(arr):
        return
    for i in range(idx, len(arr)):
        # since arr is sorted, if current element is too big to be picked to achieve target, we can skip the next elements and break here
        if arr[i] > target:
            break
        # condition to avoid duplicates by avoiding picking same element for the same position we are trying to fill in the combination
        # idx is the starting index here, not 0
        if i > idx and arr[i] == arr[i - 1]:
            continue
        comb.append(arr[i])
        findCombinations(i + 1, arr, target - arr[i], comb, resCombs)
        comb.pop()
        
def combinationSum(candidates, target):
    '''
    Since now, we use "pick and not pick" pattern which can be use here too
    The solution will be similar to the previous problem, with a single change where we move to next index after we pick or not pick
    But it would require a set data structure to avoid duplicates and it increases the complexity.

    So we are going to see another pattern now, called "sub sequence pattern".
    Since we need order to avoid duplicates, first we sort the given array.
    The idea is like this:
    Instead of iterating through the indices of given array to either pick or not pick,
    we iterate through the indices/positions of the combination blue print

    1st position:
        Here we can pick elements from index 0 to n - 1 from the array, giving each index an opportunity to be picked for 1st position
        Since the array is sorted, if we encounter a same element as previous one when iterating through the array, we skip it to avoid duplicates
        as we already picked the same element for 1st postion
        Let's say we pick 0th element for 1st position - Again start the same procedure for selection 2nd position, now iterating from 1 to n - 1

        Similar to we what we did in pick and not pick method, we need to remove the element that we picked for the 1st position before we move to next element
        and giving it the opportunity to be picked for the 1st position
    '''
    candidates.sort()
    comb = []
    resCombs = []
    findCombinations(0, candidates, target, comb, resCombs)
    return resCombs

arr = [1, 1, 1, 2, 2]
arr = [2, 1, 1, 2, 1]
target = 4
print(combinationSum(arr, target))