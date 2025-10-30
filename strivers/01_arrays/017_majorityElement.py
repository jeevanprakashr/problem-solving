# element occuring more than n/2 times
def majorityElement(arr):
    # moore's voting algorithm
    # for each element, cancel it with different element
    # if an element exists more than n/2 times, then it can't be cancelled out
    n = len(arr)
    cnt = 0
    el = -1
    for num in arr:
        if cnt == 0:
            el = num
            cnt = 1
        elif num == el:
            cnt += 1
        else:
            cnt -= 1
    resCnt = 0
    for num in arr:
        if num == el:
            resCnt += 1
    if resCnt >= n // 2:
        return el
    return -1

arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]
# arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 1, 1, 1, 1]
print(majorityElement(arr))