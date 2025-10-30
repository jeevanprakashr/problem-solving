# given array of flowers, arr[i] - no. of days required for flower i to bloom
# given k, no of consecutive flowers needed to make a bouquet
# given m, no of bouquets needed
# return minimum no of days required to get m bouquets
# if no answer possible, return -1
def minDaysForMBouquets(bloomDays, m, k):
    '''
    minimum possible day - min of bloomDays
    maximum possible day - max of bloomDays
    apply binSearch between them
    '''
    def possible(days):
        cnt = 0
        bouquets = 0
        for i in range(n):
            if bloomDays[i] <= days:
                cnt += 1
            else:
                bouquets += cnt // k
                cnt = 0
        bouquets += cnt // k
        return bouquets >= m
    
    n = len(bloomDays)
    if m * k > n:  # possible overflow
        return -1
    low = min(bloomDays)
    high = max(bloomDays)
    while low <= high:
        mid = low + ((high - low) // 2)
        if possible(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low

bloomDays = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3
print(minDaysForMBouquets(bloomDays, m, k))
