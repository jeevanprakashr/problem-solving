# Split given array into k partitions
# such that the max subarray/partition sum is the minimum
# return that minimum max subarray sum
# problem also known as painter's partition. k painters, n units to paint, partition units between painters
# subarray/partition can't be empty.
# Eg: [10, 20, 30, 40]  k = 2
# [10] [20, 30, 40]  =>  max(10, 90) = 90
# [10, 20] [30, 40]  =>  70
# [10, 20, 30] [40]  =>  60
# ans = min => 60

def paintersPartition(arr, k):
    '''
    Exact same problem as previous allocateBooks
    '''
    def numOfPainters(maxUnits):
        painters = 1
        totalUnits = 0
        for i in range(n):
            if totalUnits + arr[i] <= maxUnits:
                totalUnits += arr[i]
            else:
                painters += 1
                totalUnits = arr[i]
        return painters
    
    n = len(arr)
    if k > n:
        return -1
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = low + ((high - low) // 2)
        painters = numOfPainters(mid)
        if painters > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

arr = [10, 20, 30, 40]
k = 2
print(paintersPartition(arr, k))