# given n children, each having a rating number
# need to given candies to children
# the conditions are
# each child should get atleast a candy
# child with higher rating than its neighbours (both left and right ) should get more candies than its neighbour
# return minimum no. of candies needed

class CandyForChildren:
    def brute(self, arr):
        '''
        the condition is that
        the child with higher rating than its left and right child should get more candies than them
        So greedily we will keep the bare minimum as 1 candy
        we shall focus on left neightbors first as we go from left to right
        Then we shall focus on the right neighbors as we go from right to left as we can't focus both at once
        let see with an example
        arr =       [0, 2, 4, 3, 2, 1, 1, 3, 5, 6, 4, 0, 0]
        left =  --> [1, 2, 3, 1, 1, 1, 1, 2, 3, 4, 1, 1, 1]     at idx 3, since rating 3 is smaller than rating 4, we stick to bare minimum, 1. remember we are not focusing on right neibours
        right =     [1, 1, 4, 3, 2, 1, 1, 1, 1, 3, 2, 1, 1] <--
        now at idx 2, rating-4 is greater than 2 and 3 on both sides
        so by choosing max of both left and right arr, we can ensure that the condition won't be broken
        We shall follow the similar approach and add all the max of left and right to get our result
        max =       [1, 2, 4, 3, 2, 1, 1, 2, 3, 4, 2, 1, 1]
        '''
        n = len(arr)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        left[0] = 1
        right[n - 1] = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        for j in range(n - 2, -1, -1):
            if arr[j] > arr[j + 1]:
                right[j] = right[j + 1] + 1
            else:
                right[j] = 1
        total = 0
        for i in range(n):
            total += max(left[i], right[i])
        return total
    
    def better(self, arr):
        '''
        The above approach uses a space complexity of O(2n).
        It can be done with a single array since we only need max.
        so we shall find left array at first, for right we simply iterate and compute and find max on the iteration itself
        '''
        n = len(arr)
        left = [0 for i in range(n)]
        left[0] = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        total = max(1, left[n - 1])
        right = 1
        curr = 1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                curr = right + 1
            else:
                curr = 1
            right = curr
            total += max(left[i], curr)
        return total
    
    def optimal(self, arr):
        '''
        This approach is called slope approach. Lets try an example
        arr = [0, 2, 4, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 2, 1, 1, 1]
        lets convert this in the form of slopes

                    7
                4       6
            2               5
        0                       4                               4
                                    3                       3       2
                                        2               2               1   1   1
                                            1   1   1

        lets look the first upward slope and allot candies

                    4 <-- peak
                3   7
            2   4
        1   2
        0

        next lets look the downward slope and the candies would be alloted like
        
        7
        7   6
            6   5
                5   4
                    4   3
                        3   2
                            2   1
                                1
        
        but since we only need the the sum of the candies, the way of distribution is not important, which means the above distribution can also be converted to
        7
        7   1
            6   2
                5   3
                    4   4
                        3   5
                            2   6
                                1
        now the downPeak or simply down will be, down = 7
        we have already added 1 to 4 as our sum, then we kept adding 1 to 6 when we were in down slope to sum and down peak is 7
        down > peak => 7 > 4
        so we need to replace the added 4 with 7
        so we simply do sum += down - peak

        we repeat this same procedure for every curve (up and down)
        
        and if we see a flat line, we simply keep adding 1.
        '''
        n = len(arr)
        sm = 1
        i = 1
        while i < n:
            if arr[i] == arr[i - 1]:
                sm += 1
                i += 1
                continue
            peak = 1
            while i < n and arr[i] > arr[i - 1]:
                peak += 1   # increment peak first and then add to sm
                sm += peak
                i += 1
            down = 1
            while i < n and arr[i] < arr[i - 1]:
                sm += down  # add down to sm first and then increment down
                down += 1
                i += 1
            if down > peak:
                sm += down - peak
        return sm


sol = CandyForChildren()
arr = [0, 2, 4, 3, 2, 1, 1, 3, 5, 6, 4, 0, 0]
print(sol.brute(arr))
print(sol.better(arr))
print(sol.optimal(arr))
arr = [0, 2, 4, 7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 2, 1, 1, 1]
print(sol.optimal(arr))