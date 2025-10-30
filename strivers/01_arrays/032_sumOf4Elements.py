# unique quads with sum as given target
class SumOf4:
    def better(self, arr, target):
        n = len(arr)
        ansSt = set()
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                st = set()
                for k in range(j + 1, n):
                    sm = arr[i]
                    sm += arr[j]
                    sm += arr[k]
                    rem = target - sm
                    if rem in st:
                        quad = [arr[i], arr[j], arr[k], rem]
                        quad.sort()
                        ansSt.add(tuple(quad))
                    st.add(arr[k])
        for quad in ansSt:
            ans.append(list(quad))
        return ans
    
    def optimal(self, arr, target):
        n = len(arr)
        arr.sort()
        ans = []
        for i in range(n):
            if i != 0 and arr[i - 1] == arr[i]:
                continue
            for j in range(i + 1, n):
                if j != i + 1 and arr[j - 1] == arr[j]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    sm = arr[i]
                    sm += arr[j]
                    sm += arr[k]
                    sm += arr[l]
                    if sm == target:
                        ans.append([arr[i], arr[j], arr[k], arr[l]])
                        k += 1
                        l -= 1
                        while k < l and arr[k - 1] == arr[k]:
                            k += 1
                        while k < l and arr[l] == arr[l + 1]:
                            l -= 1
                    elif sm < target:
                        k += 1
                    else:
                        l -= 1
        return ans

sol = SumOf4()
arr = [1, 0, -1, -2, 2, 0]
arr = [1, 2, -1, -2, 2, 0, -1]
print(sol.better(arr, 0))
print(sol.optimal(arr, 0))
arr = [2, 3, 1, 5, 4, 2, 1, 3, 5, 1, 4, 3, 2, 4]
print(sol.better(arr, 8))
print(sol.optimal(arr, 8))
