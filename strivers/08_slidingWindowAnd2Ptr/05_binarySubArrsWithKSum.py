# given an array of binary nums (0/1) and k, return no. of subarrays with sum k

def binarySubArrsWithKSum(arr, k):
    '''
    This problem can also be solved by using 028_noOfSubArrsWithKSum solution
    But since that uses extra space and we have for a fact that array only contains 0 and 1, not negatives as in that problem
    we can still optimize it using sliding window.
    But staight forwardly applying sliding window here have a problem

    Lets take
    arr = [1, 0, 0, 1, 1, 0]    k = 2
    and start applying out sliding window solution

    we start l and r at index 0
    l = 0, r = 0
        subArr = [1]
        sum = 1 < 2
        so we increment r
    l = 0, r = 1
        subArr = [1, 0]
        sum = 1 < 2
        so we increment r
    
    repeating like this, we come at
    l = 0, r = 3
        subArr = [1, 0, 0, 1]
        sum = 2 = k
        we got our first sub arr
        so we increment our subarray counter
        cnt = 1
        now we move r
    l = 0, r = 4
        subArr = [1, 0, 0, 1, 1]
        sum = 3 > 2
        now by the rule of sliding window, we would start shrinking by moving l
    l = 1, r = 4
        subArr = [0, 0, 1, 1]
        sum = 2 = k
        we got another sub arr
        so cnt = 2
        now by the rule of sliding window, we would start moving r
        but if we move r, we would miss the subArr = [0, 1, 1] with l = 2, r = 4
        if we instead move l, we would miss another valid segment with l = 1, r = 5 which is [0, 0, 1, 1, 0]
        this is the problem we face, not determining which to move, l or r
    
    To solve this, we start solving another problem, which is slightly different from what was asked
    To find no. of subarrays with sum <= k, not sum == k

    let's start with the same array and k = 2
    l = 0, r = 0
        subArr = [1]
        sum = 1 <= k
        so cnt = 1
    l = 0, r = 1
        subArr = [1, 0]
        sum = 1 <= k
        now we simply don't increment our subArr counter
        we can say that even after adding an element at index r, our sum still satisifies the condition
        so the element at index r itself can form a subarray on its own
        so we need to calculate the no. of arrays that can be formed with r index element at their end
        which is r - l + 1  =>  [0], [1, 0]  =>  2
        finally we add this no. of subarrays which satisfy our condition to our counter
        cnt += 2  =>  cnt = 3
    l = 0, r = 2
        subArr = [1, 0, 0]
        sum = 1 <= k
        similar as above, the possible subarrays are [0], [0, 0], [1, 0, 0] which are 3
        so cnt = 3 + 3 = 6
    l = 0, r = 4
        subArr = [1, 0, 0, 1]
        sum = 2 <= k
        subArrs = [1], [0, 1], [0, 0, 1], [1, 0, 0, 1] => 4
        cnt = 6 + 4 = 10
    l = 0, r = 5
        subArr = [1, 0, 0, 1, 1]
        sum = 3 > k
        now, we apply the sliding window rule of shrinking by moving l
        l = 1, r = 5  (this would our inner while loop)
        subArr = [0, 0, 1, 1]
        sum = 2 <= k
        now the subarrays responding to new element at index r = 5 are [1], [1, 1], [0, 1, 1], [0, 0, 1, 1] => 4
        so cnt += 4 = 14
    
    by following this method we can find no. of subArrs with sum <= k
    our goal is no. of subArrs with sum = k
    if we think logically,
    no. of subArrs with sum k = (no. of subArrs with sum <= k) - (no. of subArrs with sum <= k - 1)
    lets say k = 4
    k - 1 = 3
    we can say that, subArrs with sum <= 3 are also subArrs with sum <= 4, since 3 < 4
    so "sum <= 4" is the super set and "sum <= 3" is its subset
    by simply removing/subtracting the subset from the superset, we would get our answer which is "sum = 4"

    note: we need to return 0 if k < 0 as negative sum is not possible in array of binaries (k - 1 can lead to k < 0 case if k = 0)
    '''
    def noOfSubArrsWithSumLTEK(arr, k):
        if k < 0:
            return 0
        n = len(arr)
        l = 0
        r = 0
        cnt = 0
        sm = 0
        while r < n:
            sm += arr[r]
            while sm > k:
                sm -= arr[l]
                l += 1
            cnt += r - l + 1
            r += 1
        return cnt
    return noOfSubArrsWithSumLTEK(arr, k) - noOfSubArrsWithSumLTEK(arr, k - 1)

arr = [1, 0, 0, 1, 1, 0]
k = 2
print(binarySubArrsWithKSum(arr, k))