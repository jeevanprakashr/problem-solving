# only one element occurs once and every other element occurs twice in the sorted array
def findSingleNonDuplicate(arr):
    '''
    Intutition:
    when a single element is not duplicate,
    every pairs on the left have indices at (even, odd)
    every pairs on the right have indices at (odd, even)
    (even, odd):
    if mid satisfies this condition, ans lies on the right, so eliminate left
    (odd, even):
    if mid satisfies this condition, ans lies on the left, so eliminate right
    '''
    n = len(arr)
    if n == 1:
        return arr[0]
    # trim down ending elements to keep the code clean of complicated edge cases inside our algo
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]
    low = 1
    high = n - 2
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid - 1] != arr[mid] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        # check for left half
        if (mid % 2 == 1 and arr[mid - 1] == arr[mid]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(findSingleNonDuplicate(arr))