# given n intervals, with overlapping intervals
# in previous problems, [1, 2] and [2, 3] are overlapping
# but here, they are not. overlapping here is [1, 3] and [2, 4] where the overlapping is crossing the border of intervals
# return the minimum no. of intervals to remove, so that the remaining intervals stay non overlapped.
# sample:
# intervals = [(1, 2), (2, 3), (3, 4), (1, 3)]
# possiblity 1:
# remove: (1, 2), (2, 3)
# remaining: (3, 4), (1, 3)  -> non overlapping
# possiblity 2:
# remove: (1, 3)
# remaining: (1, 2), (2, 3), (3, 4)  ->  non overlapping
# the minimum no. of intervals to be removed is 1 and the ans is 1

def minIntervalsToRemove(intervals):
    '''
    This is the exact same problem that we solved in 06_nMeetingsInRoom.
    There we try to maximize the meetings that can be allotted in a meeting room and return maximum no. of meetings
    by neglecting meetings with overlapping timings.
    This is a slight variation of that problem statement. Instead of returning maximum no. of meetings,
    we return no. of meetings that we neglect by simply subtracting.
    '''
    n = len(intervals)
    intervals.sort(key = lambda interval: interval[1])  # sorting with end time
    cnt = 1
    lastEndTime = intervals[0][1]
    for i in range(1, n):
        if lastEndTime <= intervals[i][0]:
            cnt += 1
            lastEndTime = intervals[i][1]
    return n - cnt

intervals = [(0, 5), (3, 4), (1, 2), (5, 9), (5, 7), (7, 9)]
intervals = [(1, 2), (2, 3), (3, 4), (1, 3)]
print(minIntervalsToRemove(intervals))