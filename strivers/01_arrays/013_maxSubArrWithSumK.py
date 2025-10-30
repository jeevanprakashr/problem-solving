class MaxSubArrWithSumK:
    def brute(self, arr, k):
        n = len(arr)
        maxLen = 0
        for i in range(n):
            sm = 0
            for j in range(i, n):
                sm += arr[j]
                if sm == k:
                    maxLen = max(maxLen, j - i + 1)
        return maxLen
    
    def better(self, arr, k):
        # can be used for arr with negatives too
        # optimal for negatives
        n = len(arr)
        prefixSum = dict()
        sm = 0
        maxLen = 0
        for i in range(n):
            sm += arr[i]
            if sm == k:
                maxLen = i + 1
            rem = sm - k
            if rem in prefixSum:
                maxLen = max(maxLen, i - prefixSum[rem])
            if sm not in prefixSum:
                prefixSum[sm] = i
        return maxLen
    
    def optimal(self, arr, k):
        # for positives only
        n = len(arr)
        left = 0
        right = 0
        maxLen = 0
        sm = arr[0]
        while right < n:
            while left <= right and sm > k:
                sm -= arr[left]
                left += 1
            if sm == k:
                maxLen = max(maxLen, right - left + 1)
            right += 1
            if right < n:
                sm += arr[right]
        return maxLen
            

arr = [1, 2, 3, 1, 1, 1, 1, 3, 3]
# arr = [2, 0, 0, 3]
k = 3
sol = MaxSubArrWithSumK()
print(sol.brute(arr, k))
print(sol.better(arr, k))
print(sol.optimal(arr, k))