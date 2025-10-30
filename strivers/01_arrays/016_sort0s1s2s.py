class Sort0s1s2s:
    def better(self, arr):
        zeros = 0
        ones = 0
        twos = 0
        for num in arr:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        i = 0
        for j in range(zeros):
            arr[i] = 0
            i += 1
        for j in range(ones):
            arr[i] = 1
            i += 1
        for j in range(twos):
            arr[i] = 2
            i += 1
    
    def optimal(self, arr):
        # Dutch national flag algorithm
        # l - low
        # m - mid
        # h - high
        # 0 . . . 0 1 . . . 1 x . . . x 2 . . . 2
        #           l         m       h
        # 0 to l - 1     -> 0s
        # l to m - 1     -> 1s
        # m to h         -> unsorted
        # h + 1 to n - 1 -> 2s
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        n = len(arr)
        low = 0
        mid = 0
        high = n - 1
        while mid <= high:
            if arr[mid] == 0:
                swap(low, mid)
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                swap(mid, high)
                high -= 1

arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sol = Sort0s1s2s()
# sol.better(arr)
sol.optimal(arr)
print(arr)