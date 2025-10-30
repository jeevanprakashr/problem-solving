# Peak element - arr[i - 1] < arr[i] and arr[i] > arr[i + 1]
# For both ends, i - 1 for the start and i + 1 for the end will be -inf
# if more than one peaks present, return any one of them
# arr[i - 1] != arr[i] i.e., there won't be any flatlines
class FindPeakElement:
    def singlePeakElement(self, arr):
        # if there is only one peak element
        '''
        if mid occurs at the increasing slope, peak is at the right
        if mid occurs at the decreasing slope, peak is at the left
        '''
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] > arr[1]:
            return 0
        if arr[n - 1] > arr[n - 2]:
            return n - 1
        low = 1
        high = n - 2
        while low <= high:
            mid = low + ((high - low) // 2)
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] > arr[mid - 1]:
                # increasing slope, eliminate left half
                low = mid + 1
            elif arr[mid] > arr[mid + 1]:
                # decreasing slope, eliminate right half
                high = mid - 1
        return -1
    
    def moreThanOnePeakElement(self, arr):
        '''
        There is another case here
        there will be a point with is the opposite of peak here, i.e., arr[i - 1] > arr[i] and arr[i + 1] > arr[i]
        if mid occurs there, the conditions we used to eliminate half in single peak scenario won't work
        so if it occurs, we can attain the solution by moving to either of the halfs, no matter which one
        other than that, the above solution works perfectly fine
        '''
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] > arr[1]:
            return 0
        if arr[n - 1] > arr[n - 2]:
            return n - 1
        low = 1
        high = n - 2
        while low <= high:
            mid = low + ((high - low) // 2)
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] > arr[mid - 1]:
                # increasing slope, eliminate left half
                low = mid + 1
            else:
                # decreasing slope or a valley (opposite of peak), eliminate right half
                high = mid - 1
        return -1

sol = FindPeakElement()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
arr = [1, 10, 13, 7, 6, 5, 4, 2, 1, 0]
arr = [5, 4, 3, 2, 1]
print(sol.singlePeakElement(arr))
arr = [1, 5, 1, 2, 1]
print(sol.moreThanOnePeakElement(arr))
