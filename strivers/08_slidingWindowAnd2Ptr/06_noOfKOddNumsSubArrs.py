# given an array of integers and k, return no. of subarrays which contain exactly k no. of odd numbers
# also called nice sub array

def noOfKOddNumsSubArrs(arr, k):
    '''
    if we convert all the odd numbers to 1 and all the even numbers to 0,
    we can see that this is the exact problem we did previously in 05_binarySubArrsWithKSum
    instead of adding or subtracting the element to sum, we need to add or subtract with 'mod 2' of the element to get 0 or 1
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
            sm += arr[r] % 2  # doing mod 2 to get 0 or 1
            while sm > k:
                sm -= arr[l] % 2  # doing mod 2 to get 0 or 1
                l += 1
            cnt += r - l + 1
            r += 1
        return cnt
    return noOfSubArrsWithSumLTEK(arr, k) - noOfSubArrsWithSumLTEK(arr, k - 1)

arr = [1, 5, 2, 1, 1]
k = 3
print(noOfKOddNumsSubArrs(arr, k))