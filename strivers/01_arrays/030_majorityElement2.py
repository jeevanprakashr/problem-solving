# elements occuring more than n/3 times
# for intuition, refer 017_majorityElement.py
def majorityElement(arr):
    n = len(arr)
    # there are atmost 2 possible numbers
    cnt1 = 0
    cnt2 = 0
    el1 = float("-inf")
    el2 = float("-inf")
    for i in range(n):
        if cnt1 == 0 and el2 != arr[i]:
            cnt1 = 1
            el1 = arr[i]
        elif cnt2 == 0 and el1 != arr[i]:
            cnt2 = 1
            el2 = arr[i]
        elif arr[i] == el1:
            cnt1 += 1
        elif arr[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if arr[i] == el1:
            cnt1 += 1
        elif arr[i] == el2:
            cnt2 += 1
    mini = (n // 3) + 1
    res = []
    if cnt1 >= mini:
        res.append(el1)
    if cnt2 >= mini:
        res.append(el2)
    res.sort()
    return res

arr = [1, 3, 1, 2, 1, 2, 1, 2]
arr = [2, 1, 1, 3, 1, 4, 5, 6]
print(majorityElement(arr))