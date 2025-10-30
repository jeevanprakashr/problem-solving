# given two sorted arrays of different or same length
# merge them and return the median
# median -> no. of elements to the left of median = no. of elements to the right of median
# if even no of elements in merged arr, (sum of middle two elements) / 2
def medianOf2SortedArrs(arr1, arr2):
    '''
    brute: merge two sorted arrs into a new array and find the median
    better: instead of using an extra new array to merge, just track the needed indices and find the median
    optimal: using binary search

    lets see with an even no. of elements example.
    arr1 = [1, 3, 4, 7, 10, 12]
    arr2 = [2, 3, 6, 15]
    
    we know the median splits the arr into two halfs.
    we are going to split the elements in each array to left and right halves.
    we need to pick only the left half elements and the right half elements wiil result themselves

    Left half will have first x elements from arr1 and first y elements from arr2 such that
    x + y = n / 2    => n is 10 in our example
          = 5

    There will be exacly one correct way of splitting
    we are going to do binary search for x

    range of x will be 0 (no elements in arr1) to 6 (all elements in arr1)

    x = 0:
        if we pick no element from arr1, then we need to use arr2 to make up 5 elements of left side
        but arr2 has only 4 elements. so 0 doesn't satisfy the split
    x = 1:
        taking 1 element from arr1, the split would be like

        1           | 3, 4, 7, 10, 12
        2, 3, 6, 15 |

        lets l1 - max element on left from arr1         r1 - min element on right from arr1
             l2 - max element on right from arr2        r2 - min element on right from arr2
        satisfying condition for a correct split is
            l1 < r2 and l2 < r1
        as l1 < r1 and l2 < r2 is already an established fact as they are from same sorted arrays respectively
        in our case 15 > 3 which violates l2 < r1
        so 1 is not our answer
    x = 2:
        taking 2 elements from arr1

        1, 3    | 4, 7, 10, 12
        2, 3, 6 | 15

        6 > 4 and hence 2 is not our answer
    x = 3
        taking 3 elements from arr1
        1, 3, 4 | 7, 10, 12
        2, 3    | 6, 15
        4 < 6 and 3 < 7 and hence 3 is our answer
    x = 4
        takind 4 elements form arr1
        1, 3, 4, 7 | 10, 12
        2          | 3, 6, 15
        7 > 3 and so 4 is not our answer
    the same goes for x = 5 and x = 6 

    the pattern here is
    0, 1, 2, 3, 4, 5, 6
    x, x, x, o, x, x, x

    now lets see the logic of whether to move left or right as our general binary search pattern doesn't follow here

    lets say x = 2
        we have 6 > 4, 6 from arr2 and 4 from arr1
        in order for this to settle is for 6 to go away towards right side
        if 6 goes away to right then 4 from arr1 should come to left
        if 4 comes to left, that increase our x = 2 condition to x = 3

        thus we move towards right side in our binary search which means
        low = mid + 1
    
    if x = 4
        we have 7 > 3, 7 from arr1 and 3 from arr2
        to settle this 7 should move to right but 7 is from arr1
        if 7 from arr1 goes to right, then 3 from arr2 goes to left
        this decreases our x = 4 condition to x = 3

        thus we move towards left side in our binary search which means
        high = mid - 1
    
    so the condition here is
    if l1 > r2, move left  =>  high = mid - 1
    if l2 > r1, move right =>  low = mid + 1

    Trick: choose arr with shorter length as arr1 to do the binary search, so it results in much lesser time complexity

    once we split the array into left and right, we can find median like
    median = (max(l1, l2) + min(r1, r2)) / 2

    Odd case:
    Eg: arr1 = [2, 4]
        arr2 = [1, 3, 5]
    Instead of doing an equal split, do the unequal split
    left - 3, right - 2     or      left - 2, right - 3
    median will be on               median will be on right side
    left side
    median = max(l1, l2)            median = min(r1, r2)

    we will go for median on left side, since the formula for no. of left elements will satisfy both even and odd cases
    x = (n1 + n2 + 1) // 2
    if n = 10 (even)
        x = (10 + 1) // 2 = 5  =>  5 on left
    if n = 5 (odd)
        x = (5 + 1) // 2 = 3   =>  3 on left

    Note: if any of l1, l2, r1, r2 doesn't exist, consider them to be the most possible value
    l1 and l2  ->  -inf
    r1 and r1  ->  +inf
    '''
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 > n2:
        # do bs on shorted array
        return medianOf2SortedArrs(arr2, arr1)
    n = n1 + n2
    left = (n1 + n2 + 1) // 2
    low = 0
    high = n1
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        l1 = float("-inf")
        l2 = float("-inf")
        r1 = float("+inf")
        r2 = float("+inf")
        if mid1 < n1:
            r1 = arr1[mid1]
        if mid2 < n2:
            r2 = arr2[mid2]
        if mid1 - 1 >= 0:
            l1 = arr1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = arr2[mid2 - 1]
        if l1 <= r2 and l2 <= r1:
            if n % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
        '''elif l2 > r1:
            low = mid1 + 1
        else:
            high = mid1 - 1'''
    return 0  # dummy return

arr1 = [1, 3, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]

arr1 = [1, 3, 4]
arr2 = [2, 5]
print(medianOf2SortedArrs(arr1, arr2))