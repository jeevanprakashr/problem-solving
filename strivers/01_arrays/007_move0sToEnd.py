def move0sToEnd(arr):
    n = len(arr)
    first0 = -1
    for i in range(n):
        if arr[i] == 0:
            first0 = i
            break
    if first0 == -1:
        return
    for i in range(first0 + 1, n):
        if arr[i] != 0:
            arr[first0], arr[i] = arr[i], arr[first0]
            first0 += 1

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
move0sToEnd(arr)
print(arr)