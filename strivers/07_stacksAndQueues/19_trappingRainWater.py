# Given an arr of positive integers where arr[i] represents the height of a building which can be 0 as well
# if it rains, return the total units of space that can be occupied by the water in between buildings
# Eg: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#         1           4           1         =   6

class TrapRainWater:
    def approach1(self, arr):
        '''
        Intuition:
        If we keep on adding how much water is logged on top of every building, we can find our answer
        How much water logged on top:
            For a building, if we somehow figure out the max height building to the left and to the right,
            we can say the water will be logged upto the smaller height building among those to max buildings.
            And to find the actual units of water logged above the building
            units of water logged = min(leftMax, rightMax) - height(building)
            If we keep on adding this for all the buildings, we get our answer
        How to find leftMax and rightMax:
            Precompute two arrays prefixMax and suffixMax to record the max element upto each ith index from the start and from the end respectively
            which will give our leftMax and rightMax
        '''
        n = len(arr)
        suffixMax = [0 for _ in range(n)]
        suffixMax[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(arr[i], suffixMax[i + 1])
        total = 0
        leftMax = 0
        for i in range(n):
            leftMax = max(leftMax, arr[i])
            rightMax = suffixMax[i]
            if arr[i] < leftMax and arr[i] < rightMax:
                total += min(leftMax, rightMax) - arr[i]
        return total
    
    def approach2(self, arr):
        '''
        Optimal one compared to above solution
        The idea is based on the fact that, if we need only the min of leftMax and rightMax, then we only need one of them, the minimum
        We use a two pointer approach here, l and r
        and we iterate only the smaller one at a time since we need only the smaller
        also we maintain leftMax and rightMax variables while iterating
        '''
        n = len(arr)
        l = 0
        r = n - 1
        leftMax = 0
        rightMax = 0
        total = 0
        while l < r:
            if arr[l] <= arr[r]:
                if leftMax > arr[l]:
                    total += leftMax - arr[l]
                else:
                    leftMax = arr[l]
                l += 1
            else:
                if rightMax > arr[r]:
                    total += rightMax - arr[r]
                else:
                    rightMax = arr[r]
                r -= 1
        return total

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sol = TrapRainWater()
print(sol.approach1(arr))
print(sol.approach2(arr))