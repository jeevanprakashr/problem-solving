# given arrival and departure times of n trains for a station in a form of 2 arrays, arrival array and departure array
# return minimum no. of platforms needed to accomodate all the trains in the station according to their times.
# sample:
# arr = [900, 945, 955, 1100, 1500, 1800]
# dep = [920, 1200, 1130, 1150, 1900, 2000]
# the first train arrives at 9.00 am and leaves at 9.20 am
# atleast 3 platforms are needed to accomodate the timings, so the ans is 3

def minPlatformsForRailwayStation(arr, dep):
    '''
    we can see that if we find the maximum no. of intersecting trains at a time, we get our answer.
    checking of intersection for a train with the target train would be checking if
    target train:               arr                 dep
    possible     :      arr1                                dep1
    intersections       arr2                dep2
                                            arr3            dep3
                                    arr4    dep4
    so there are 4 possible intersections

    our brute force approach would be finding no. of intersecting trains for each train link
    for i (0 -> n)
        for j (i+1 -> n)
            if intersect(i, j)
    and find the max intersecting trains

    better approach:
    treat arrival and departure as events happening in timely (sorted) manner
    keep a counter
    increment it for arrival and decrement it for departure. return max value of counter
    we form a new array containing arrival and departure events together in sorted timely manner

    (900, A), (920, D), (945, A), (955, A), (1100, A), (1130, D), ...

    with this we can iterate and update our counter accordingly

    optimal:
    instead of forming a new array clubbing both arrival and departures,
    we just sort both arrival and departure arrays independently and have two pointer approach similar to merge sort
    one pointer starting in arrival and one pointer starting in departure and we move pointers accordingly and update our counter
    '''
    n = len(arr)
    arr.sort()
    dep.sort()
    i = 0
    j = 0
    cnt = 0
    maxCnt = 0
    while i < n:    # since arrival time will exhaust first
        if arr[i] <= dep[j]:
            i += 1
            cnt += 1
        else:
            j += 1
            cnt -= 1
        maxCnt = max(maxCnt, cnt)
    return maxCnt

arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
print(minPlatformsForRailwayStation(arr, dep))