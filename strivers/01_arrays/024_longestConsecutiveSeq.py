class LongestConsecutiveSeq:
    # [102, 4, 100, 1, 101, 3, 2, 1, 1]
    # cons. seq. 1 - [100, 101, 101] - 3
    # cons. seq. 2 - [1, 2, 3, 4] - 4
    # ans = 4
    def better(self, arr):
        arr.sort()
        n = len(arr)
        lastSmaller = float("-inf")
        longest = 1
        cnt = 0
        for i in range(n):
            if arr[i] - 1 == lastSmaller:
                cnt += 1
                lastSmaller = arr[i]
            elif arr[i] != lastSmaller:
                cnt = 1
                lastSmaller = arr[i]
            longest = max(longest, cnt)
        return longest
    
    def optimal(self, arr):
        n = len(arr)
        longest = 0
        st = set()
        for num in arr:
            st.add(num)
        for num in st:
            if num - 1 in st:
                continue
            cnt = 1
            x = num
            while x + 1 in st:
                cnt += 1
                x += 1
            longest = max(longest, cnt)
        return longest

arr = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2]
arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
sol = LongestConsecutiveSeq()
print(sol.better(arr))
print(sol.optimal(arr))
