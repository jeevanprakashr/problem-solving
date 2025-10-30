# merge 2 sorted arrays without using extra space
# Eg: [1, 3, 5, 7]  [0, 2, 6, 8, 9]  =>  [0, 1, 2, 3]  [5, 6, 7, 8, 9]
class MergeSortedArrsInPlace:
    def solutionOne(self, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        left = n - 1
        right = 0
        while left >= 0 and right < m:
            if arr1[left] > arr2[right]:
                arr1[left], arr2[right] = arr2[right], arr1[left]
                left -= 1
                right += 1
            else:
                break
        arr1.sort()
        arr2.sort()
    
    def solutionTwo(self, arr1, arr2):
        # gap method - based on shell sort algorithm
        def swapIfGreater(arr1, arr2, ind1, ind2):
            if arr1[ind1] > arr2[ind2]:
                arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]
        
        n = len(arr1)
        m = len(arr2)
        ln = n + m
        gap = (ln // 2) + (ln % 2)   # divide by 2 and take the ceil value Eg: 9 / 2 = 4.5 = 5
        while gap > 0:    # O(log (ln))
            left = 0
            right = left + gap
            while right < ln:    # O(ln)
                if left < n and right >= n:
                    # left in arr1, right in arr2
                    swapIfGreater(arr1, arr2, left, right - n)
                elif right < n:
                    # left and right in arr1
                    swapIfGreater(arr1, arr1, left, right)
                else:
                    # left and right in arr2
                    swapIfGreater(arr2, arr2, left - n , right - n)
                left += 1
                right += 1
            if gap == 1:
                break
            gap = (gap // 2) + (gap % 2)


arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
sol = MergeSortedArrsInPlace()
# sol.solutionOne(arr1, arr2)
sol.solutionTwo(arr1, arr2)
print(arr1, arr2)