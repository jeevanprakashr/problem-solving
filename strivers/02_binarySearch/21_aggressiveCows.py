# Given arr of stalls, arr[i] - coordinate of stall i in a single dimention
# Given k cows
# place k cows among the stalls such that the minumum distance between any two cows is the maximum
# [0, 3, 4, 7, 10, 9], k = 4
# => [0, 3, 4, 7, 9, 10]  =>  Sorted so that checking the distance between consecutive stalls is enough
# D(s1, s2) > D(s1, s3) as s2 lies between s1 and s3
# since goal is to find minimum between any two cows, D(s1, s3) won't matter, hence sorted the stalls
# [c1, c2, c3, c4, -, -]
# [  3   1   3         ]  =>  1

# [c1, -, c2, -, c3, c4]
# [    4      5    1   ]  =>  1

# [c1, -, c2, c3, -, c4]
# [    4    3     3    ]  =>  3

# the max of all these possible min distances is 3 and hence the answer is 3
def aggressiveCows(arr, k):
    '''
    Lets find the range for answer
    min is 1
    max is max(arr) - min(arr) since mininum number of cows is 2 and best possible way to allote them to maximize the distance is at min and max positions
    To find if the answer is possible:
    only place a cow at a stall if the distance between previous placed cow is greater than or equal to the answer under investigation
    so to be greedy, always place the first cow at first position as it doesn't need previous cow to check
    1 - [c1, c2, c3, c4, -, -] - possible
        [  3   1   3         ]
    2 - [c1, c2, -, c3, c4, -] - possible
        [  3     4    2      ]
    3 - [c1, c2, -, c3, -, c4] - possible
        [  3     4      3    ]
    4 - [c1, -, c2, -, c3. -]  - c4 can't be placed hence not possible
        [    4      5       ]
    if 4 is not possible then definitely anything greater than 4 is not possible
    '''
    def possible(minDistance):
        placedCows = 1
        last = arr[0]
        for i in range(1, n):
            if arr[i] - last >= minDistance:
                placedCows += 1
                last = arr[i]
            if placedCows >= k:
                return True
        return False
    n = len(arr)
    arr.sort()
    low = 1
    high = arr[n - 1] - arr[0]
    while low <= high:
        mid = low + ((high - low) // 2)
        if possible(mid):
            low = mid + 1
        else:
            high = mid - 1
    return high

arr = [0, 3, 4, 7, 10, 9]
k = 4
print(aggressiveCows(arr, k))