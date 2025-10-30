# inversion - a pair (arr[i], arr[j]) where arr[i] > arr[j], i < j
'''
We are going to use merge sort to solve this
Intuition:
Consider merging two sorted arrays and count the inversion pairs between those two arrays while merging
Eg:
arr1 = [2, 3, 5, 6]    arr2 = [2, 2, 4, 4, 8]
left of the pair is from arr1 and right of the pair is from arr2
1. (2, 2)
   both equal, add right 2 to merged array and increment left (merge algo)   -    [2]
   Note (not mentioned in video): if equal, must move left pointer, not the right.
                                  in actual merge sort, it doesn't matter which one we move
                                  but for this problem, it only works if we move left pointer
2. (3, 2)
   - this is an inversion pair
   - but since it is an inversion, all the elements to the right of 3 in arr1 will also make inversion with 2 from arr2
   - so instead of increment inversion count to 1, increment with no of elements from 3 to the right in arr1, i.e., 3
   - continue with merge algo - add 2 to merged arr and increment right    -    [2, 2]
3. (3, 2)
   - Same as before
Similiarly if we continue with merge algorithm, we will get the final count of inversions.

We are going to apply the same logic in this solution
Do a plain merge sort
Eg: [5, 3, 2, 4, 1]

keep splitting the array to make two sorted arrays

[5] and [3] are sorted two arrays
While merging them, apply the above logic and track the inversions count

Lastly, we would get like [2, 3, 5] and [1, 4]
the pairs count in [2, 3, 5] were already found while merging them and the same goes for [1, 4]

'''
def countInversions(arr):
    def merge(arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        invPairs = 0    # logic for our solution
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                invPairs += mid - left + 1      # logic for our solution
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        return invPairs     # logic for our solution
    
    def mergeSort(arr, low, high):
        invPairs = 0    # logic for our solution
        if low >= high:
            return invPairs     # logic for our solution
        mid = (low + high) // 2
        invPairs += mergeSort(arr, low, mid)
        invPairs += mergeSort(arr, mid + 1, high)
        invPairs += merge(arr, low, mid, high)
        return invPairs     # logic for our solution
    
    n = len(arr)
    return mergeSort(arr, 0, n - 1)

arr = [5, 3, 2, 4, 1]
# arr = [2, 3, 5, 6, 2, 2, 4, 4, 8]
print(countInversions(arr))
print(arr)

