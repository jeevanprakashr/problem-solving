class Solution(object):
    def quickSort(self, nums, start, end):
        print(start, end)
        if start >= end:
            return
        pivot = start
        i = start + 1
        j = end
        while i <= j:
            if nums[i] <= nums[pivot]:
                i += 1
                continue
            if nums[j] > nums[pivot]:
                j -= 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
        nums[pivot], nums[j] = nums[j], nums[pivot]
        self.quickSort(nums, start, j - 1)
        self.quickSort(nums, j + 1, end)

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastPerm = True
        n = len(nums)
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                continue
            else:
                lastPerm = False
                break
        if lastPerm:
            i = 0
            j = n - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return
        i = n - 2
        while i >= 0:
            mn = float('inf')
            idx = -1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    diff = nums[j] - nums[i]
                    if diff < mn:
                        mn = diff
                        idx = j
            if idx > 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                self.quickSort(nums, i + 1, n - 1)
                break
            i -= 1
        
s = Solution()
nums = [1, 2, 3]
s.nextPermutation(nums)
print(nums)