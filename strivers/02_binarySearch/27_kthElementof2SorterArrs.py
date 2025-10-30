# find the kth element in 2 sorted arrays after merging them
def kthElementOf2SortedArrs(arr1, arr2, k):
    '''
    We will use the same concept that we used in 24_medianOf2SortedArrs
    There we tried to split the array into equal parts (even) or almost equal (odd).
    Here we will try to split at kth position
    i.e, left -> k
         right -> n - k
    and to find the kth element,
    kth element = max(l1, l2)
    we don't need r1 and r2 as the split is after the kth element and kth element will be on the left side

    using the same low and high as before won't work here as the split is not equal
    Eg:
    lets say n1 = 5, n2 = 6
    reminder x - no of elemnents to be picked from arr1 to satisfy the split
    high:
        if k = 2
        since the left should contain only 2 elements, if x = n1 = 5
        5 elements will be picked from arr1 for the left side and it breaches the 2 elements on the left condition
        so the high should be like this
        high = min(k, n1)
    low:
        lets say k = 7
        that means there should be 7 elements on the left side
        to satisfy this, even if we include all the elements from arr2 on the left side which is 6
        we still need 1 eleement from arr1
        arr1 [               1] | [2, 3, 4, 5]
        arr2 [1, 2, 3, 4, 5, 6] |
        so the low should be like this
        low = max(0, k - n2)        => even if k = 2, low = max(0, -4) = 0
    every other things will be the same as before
    '''
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 > n2:
        # do bs on shorted array
        return kthElementOf2SortedArrs(arr2, arr1, k)
    left = k
    low = max(0, k - n2)
    high = min(k, n1)
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

arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 4
print(kthElementOf2SortedArrs(arr1, arr2, k))