# given an array of unsorted overlapping intervals
# return sorted merged intervals after merging overlapping intervals

def mergeIntervals(intervals):
    '''
    First sort the intervals and merge them
    '''
    intervals.sort(key = lambda interval: (interval[0], interval[1]))
    res = []
    n = len(intervals)
    if n == 0:
        return res
    mergingInterval = [intervals[0][0], intervals[0][1]]
    for interval in intervals:
        if interval[0] <= mergingInterval[1]:
            mergingInterval[1] = max(interval[1], mergingInterval[1])
        else:
            res.append(mergingInterval)
            mergingInterval = [interval[0], interval[1]]
    res.append(mergingInterval)
    return res

intervals = [[1, 3], [2, 6], [8, 10], [8, 9], [9, 11], [15, 18], [2, 4], [16, 17]]
print(mergeIntervals(intervals))
