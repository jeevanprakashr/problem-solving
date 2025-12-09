# given an array of sorted non overlapping intervals and a single interval
# insert the interval into the array of intervals
# if it results in overlapping, merge the overlapping intervals into one and replace them

def insertInterval(intervals, newInterval):
    '''
    we can split the intervals into three parts,
    ordered left intervals, overlapping interval along with new interval and ordered right intervals
    overlapping can be done by taking min and max of all the overlapping intervals and make them into our new interval as (min, max)
    '''
    n = len(intervals)
    res = []
    i = 0
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= newInterval[1]:
        # cases: a1 b1 is the new interval
        #       a     b
        #   a1     b1
        #          a1       b1
        #       a1 b1
        #          a1 b1
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)
    while i < n:
        res.append(intervals[i])
        i += 1
    return res

intervals = [[1, 2], [3, 4], [5, 7], [8, 10], [12, 16]]
newInterval = [6, 8]
print(insertInterval(intervals, newInterval))
        