# given an array of increasing positive numbers and k, find the kth missing number in the order of 1 - n numbers
# Eg: [2, 3, 4, 7, 11], k = 5
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  =>  missing - [1, 5, 6, 8, 9, 10]
# 5th missing - 9
class KthMissingPositiveNumber:
    def brute(self, arr, k):
        '''
        Intuition:
        Let's say arr starts with 5 as [5, 8, ..] and k = 4
        we can straight away say 4 is the answer
        if k = 6
        then 6 can't be answer like before because 5 takes up 1 place, so we must add that taken up 1 place to k and k becomes 7 which is the answer
        but if we something lesser than k occupies at the start, then it takes 1 place and thus k increases
        [2, 3, 4, 7, 11], k = 5
        2 <= k (5) -> k = 6
        3 <= k (6) -> k = 7
        4 <= k (7) -> k = 8
        7 <= k (8) -> k = 9
        11 > k (9) -> hence ans is 9
        '''
        n = len(arr)
        for i in range(n):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k
    
    def optimal(self, arr, k):
        '''
        Lets set our goal to find the two adjacent indices between which our missing elements lies
        [2, 3, 4, 7, 11]
        Lets find how many missing elements at each index
        the arr should be [1, 2, 3, 4, 5] but it is [2, 3, 4, 7, 11]
        - at index 0, instead of 1, 2 appeared => missing elements => 2 - 1 = 1
        - at index 1, instead of 2, 3 appeared => missing elements => 3 - 2 = 1
        - at index 2, instead of 3, 4 appeared => missing elements => 4 - 3 = 1
        - at index 3, instead of 4, 7 appeared => missing elements => 7 - 4 = 3
        - at index 4, instead of 5, 11 appeared => missing elements => 11 - 5 = 6
        so we got [1, 1, 1, 3, 6]
        we can see our 5th missing element lies between 3 and 6 which corresponds to 7 and 11
        once we find this two indices, we can find our ans like
        at the place of 7, 4 should be there and missing elements => 3
        we need 2 more to make k = 5
        so 7 + 2 = 9 is our answer

        using BS, our indices will be at high, low (opposite polarity low started at minimum missing smaller than k and high started at maximum missing higher that k)
        high pointing at 7
        low pointing at 11
        formula derivation:
            missing at high = arr[high] - (high + 1)  {+1 bcz of index}
                            = arr[high] - high - 1
            more needed = k - missing at high
            ans = arr[high] + more needed
                = arr[high] + k - missing at high
                = arr[high] + k - (arr[high] - high - 1)
                = arr[high] + k - arr[high] + high + 1
                = high + 1 + k
            => high + 1 = low
            => ans = low + k
        '''
        n = len(arr)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            missing = arr[mid] - (mid + 1)
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k

arr = [2, 3, 4, 7, 11]
k = 5
sol = KthMissingPositiveNumber()
print(sol.brute(arr, k))
print(sol.optimal(arr, k))