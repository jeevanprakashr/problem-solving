# there is a single meeting room which a allow a single meeting at a time
# given timings of n meetings in two arrays, start time array and end time array
# time intervals of two meetings can't overlap, like (0, 5) and (5, 6) is overlapping and not allowed
# return maximum number of meetings that can be allowed
# order of meetings allowed should also be returned

def nMeetingsIn1Room(start, end):
    '''
    the greedy approach here would allot meetings which end earlier so that next meeting can be alloted sooner.
    for that we would sort the arrays based on end time and start from the second meeting in the sorted format
    as the first meeting would obviously be alloted.
    every time we allot the meeting, we track the end time as the free time so that we can evaluate the next meeting
    using whether its start time is greater than the last free time
    also we track the position too while sorting
    '''
    meetings = []
    n = len(start)
    for i in range(n):
        meetings.append((start[i], end[i], i + 1))
    meetings.sort(key = lambda x: x[1])
    allotedOrder = [meetings[0][2]]
    allotedMeetings = 1
    freeTime = meetings[0][1]
    for i in range(1, n):
        st = meetings[i][0]
        ed = meetings[i][1]
        pos = meetings[i][2]
        if st > freeTime:
            allotedOrder.append(pos)
            allotedMeetings += 1
            freeTime = ed
    return allotedMeetings, allotedOrder

start = [0, 3, 1, 5, 5, 8]
end = [5, 4, 2, 9, 7, 9]
print(nMeetingsIn1Room(start, end))