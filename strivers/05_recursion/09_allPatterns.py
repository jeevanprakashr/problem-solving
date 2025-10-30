def allSubSequencesWithSumK(arr, k):
    '''
    Given an array of numbers, print all the sub sequences whose sum is k
    Eg: arr = [1, 2, 1], k = 2
    sol = [1, 1] and [2]

    Pattern:
    The pattern we are going to see is the common and most important pattern that will be mostly used in recursion questions
    The pattern is - chosen and not chosen
    i.e, for every index, there are only two possible outcomes that need to be covered. Either chosen or not chosen
    note: for not chosen outcome, pop the element that was chosen for chosen outcome before
    '''
    def copyArr(a):
        b = []
        for num in a:
            b.append(num)
        return b
    
    def getSubSequence(idx, total, comb):
        if idx == n:
            if total == k:
                res.append(copyArr(comb))
            return
        comb.append(arr[idx])
        getSubSequence(idx + 1, total + arr[idx], comb)
        comb.pop()
        getSubSequence(idx + 1, total, comb)
    
    n = len(arr)
    res = []
    getSubSequence(0, 0, [])
    return res

def anyOneSubSequenceWithSumK(arr, k):
    '''
    No need for all the subsequences as we did above. return the first one
    for this we use return true/false to break the further recursions
    '''
    def copyArr(a):
        b = []
        for num in a:
            b.append(num)
        return b
    
    def getSubSequence(idx, total, comb):
        if idx == n:
            if total == k:
                res.append(copyArr(comb))
                return True
            return False
        comb.append(arr[idx])
        if getSubSequence(idx + 1, total + arr[idx], comb):
            return True
        comb.pop()
        if getSubSequence(idx + 1, total, comb):
            return True
        return False
    
    n = len(arr)
    res = []
    getSubSequence(0, 0, [])
    return res

def countOfSubSequenceWithSumK(arr, k):
    '''
    Instead of returning true or false as we did above, return 0 or 1 and add them up while backtracking
    '''
    def getSubSequence(idx, total):
        # if arr has only positives
        '''
        if total > k:
            return 0
        '''
        if idx == n:
            if total == k:
                return 1
            return 0
        l = getSubSequence(idx + 1, total + arr[idx])
        r = getSubSequence(idx + 1, total)
        return l + r
    
    n = len(arr)
    count = getSubSequence(0, 0)
    return count


arr = [1, 2, 1]
k = 2
print(allSubSequencesWithSumK(arr, k))
print(anyOneSubSequenceWithSumK(arr, k))
print(countOfSubSequenceWithSumK(arr, k))
