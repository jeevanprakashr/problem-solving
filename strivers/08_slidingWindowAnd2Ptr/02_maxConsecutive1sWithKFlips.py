# given array of 0's and 1's and k, return max length of consecutive 1's after flipping atmost k 0's

class MaxConsecutiveOnes:
    def better(self, arr, k):
        '''
        this problem can be rephrased like to return the max subarray with atmost k 0s
        with this we can apply sliding window to solve this problem like
        l and r pts start at 0th index
        r moves till end of the array
        count no. of zeros
        if zeros exceed k, move l pts until zeros come under k
        track the max length of the subarray window
        '''
        n = len(arr)
        l = 0
        r = 0
        zeros = 0
        res = 0
        while r < n:
            if arr[r] == 0:
                zeros += 1
            while zeros > k:
                if arr[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                res = max(res, r - l + 1)
            r += 1
        return res
    
    def optimal(self, arr, k):
        '''
        In above solution, we use O(2N) approach which is acceptable
        but it can be improved to O(N)
        by changing the inner while loop
        in the inner loop we make l to iterate until zeros come under k
        we achieve the same result by just incrementing l to l + 1
        the calculation and comparison of max length is retricted until zeros equals to k
        and we increment r as usual
        Its like making the window size rigid and unmodifiable but only capable of moving the entire window
        instead of the l and r pointers independently
        once l encounter 0 and zeros equals to k, the window comes back to flexible with independently movable r and l pointers
        '''
        n = len(arr)
        l = 0
        r = 0
        zeros = 0
        res = 0
        while r < n:
            if arr[r] == 0:
                zeros += 1
            if zeros > k:
                if arr[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                res = max(res, r - l + 1)
            r += 1
        return res

arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
sol = MaxConsecutiveOnes()
print(sol.better(arr, k))
print(sol.optimal(arr, k))