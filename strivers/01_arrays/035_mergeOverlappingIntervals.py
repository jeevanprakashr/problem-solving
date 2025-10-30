def mergeOverlappingIntervals(arr):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if len(ans) == 0 or ans[-1][1] < arr[i][0]:
            ans.append(arr[i])
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans

intervals = [[1, 3], [2, 6], [8, 9], [9, 11], [8, 10], [2, 4], [15, 18], [16, 17]]
print(mergeOverlappingIntervals(intervals))