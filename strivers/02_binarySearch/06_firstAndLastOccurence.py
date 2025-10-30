# find the first and last occurence of the given x in a sorted array with duplicates
class FirstAndLastOccurence:
    def solutionOne(self, arr, x):
        # uses 02_lowerBound and 03_upperBound
        def lowerBound(arr, n, target):
            low = 0
            high = n - 1
            ans = n
            while low <= high:
                mid = low + ((high - low) // 2)
                if arr[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        
        def upperBound(arr, n, target):
            low = 0
            high = n - 1
            ans = n
            while low <= high:
                mid = low + ((high - low) // 2)
                if arr[mid] > target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans
        
        n = len(arr)
        lb = lowerBound(arr, n, x)
        if lb == n or arr[lb] != x:
            return [-1, -1]
        return [lb, upperBound(arr, n, x) - 1]
    
    def solutionTwo(self, arr, x):
        # uses binary search two times to find first and last
        def firstOccurence(arr, n, x):
            first = -1
            low = 0
            high = n - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                if arr[mid] == x:
                    first = mid
                    high = mid - 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return first
        
        def lastOccurence(arr, n, x):
            last = -1
            low = 0
            high = n - 1
            while low <= high:
                mid = low + ((high - low) // 2)
                if arr[mid] == x:
                    last = mid
                    low = mid + 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return last
        
        n = len(arr)
        first = firstOccurence(arr, n, x)
        if first == -1:
            return [-1, -1]
        last = lastOccurence(arr, n, x)
        return [first, last]

sol = FirstAndLastOccurence()
arr = [2, 4, 6, 8, 8, 8, 11, 13]
x = 8
# x = 10
print(sol.solutionOne(arr, x))
print(sol.solutionTwo(arr, x))

# problem 2: Count the occurences of x in the given sorted arr
# same solution should be used
first, last = sol.solutionOne(arr, x)
if first == -1:
    print(0)
else:
    print(last - first + 1)