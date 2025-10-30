class EqualPosNegs:
    def brute(self, arr):
        ln = len(arr)
        pos = []
        neg = []
        for n in arr:
            if n < 0:
                neg.append(n)
            else:
                pos.append(n)
        for i in range(ln // 2):
            arr[i * 2] = pos[i]
            arr[(i * 2) + 1] = neg[i]
        return arr
    
    def optimal(self, arr):
        ln = len(arr)
        res = [0 for i in range(ln)]
        pos = 0
        neg = 1
        for n in arr:
            if n < 0:
                res[neg] = n
                neg += 2
            else:
                res[pos] = n
                pos += 2
        return res

class UnEqualPosNegs:
    def optimal(self, arr):
        n = len(arr)
        pos = []
        neg = []
        for num in arr:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        if len(pos) > len(neg):
            for i in range(len(neg)):
                arr[i * 2] = pos[i]
                arr[(i * 2) + 1] = neg[i]
            idx = len(neg) * 2
            for i in range(len(neg), len(pos)):
                arr[idx] = pos[i]
                idx += 1
        else:
            for i in range(len(pos)):
                arr[i * 2] = pos[i]
                arr[(i * 2) + 1] = neg[i]
            idx = len(pos) * 2
            for i in range(len(pos), len(neg)):
                arr[idx] = neg[i]
                idx += 1
        return arr

arr = [3, 1, -2, -5, 2, -4]
sol = EqualPosNegs()
print(sol.brute(arr))
arr = [-1, 2, 3, 4, -3, 1]
sol = UnEqualPosNegs()
print(sol.optimal(arr))
