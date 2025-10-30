def leadersOfArr(arr):
    # leader - all elements to the right are smaller
    n = len(arr)
    mx = float("-inf")
    res = []
    for i in range(n - 1, -1, -1):
        if arr[i] > mx:
            res.append(arr[i])
            mx = arr[i]
    res.sort()
    return res

arr = [10, 22, 12, 3, 0, 6]
print(leadersOfArr(arr))