def reverse_arr(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def leftRotate(arr, k):
    n = len(arr)
    k = k % n
    reverse_arr(arr, 0, k - 1)
    reverse_arr(arr, k, n - 1)
    reverse_arr(arr, 0, n - 1)

def rightRotate(arr, k):
    n = len(arr)
    k = k % n
    reverse_arr(arr, 0, n - k - 1)
    reverse_arr(arr, n - k, n - 1)
    reverse_arr(arr, 0, n - 1)

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
leftRotate(arr, k)
# rightRotate(arr, k)
print(arr)