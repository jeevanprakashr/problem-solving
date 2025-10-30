# unique triplets with sum as 0
class SumOf3:
    def better(self, arr):
        n = len(arr)
        ansSt = set()
        ans = []
        for i in range(n):
            st = set()
            for j in range(i + 1, n):
                rem = -(arr[i] + arr[j])
                if rem in st:
                    triplet = [arr[i], arr[j], rem]
                    triplet.sort()
                    ansSt.add(tuple(triplet))
                st.add(arr[j])
        for trip in ansSt:
            ans.append(list(trip))
        return ans
    
    def optimal(self, arr):
        n = len(arr)
        arr.sort()
        ans = []
        for i in range(n):
            if i > 0 and arr[i - 1] == arr[i]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sm = arr[i] + arr[j] + arr[k]
                if sm < 0:
                    j += 1
                elif sm > 0:
                    k -= 1
                else:
                    ans.append([arr[i], arr[j], arr[k]])
                    j += 1
                    k -= 1
                    while j < k and arr[j - 1] == arr[j]:
                        j += 1
                    while j < k and arr[k] == arr[k + 1]:
                        k -= 1
        return ans

sol = SumOf3()
arr = [-1, 0, 1, 2, -1, -4]
arr = [-2, -1, -1, -2, -1, 0 , -2, 2, 0, 2, 2, 0, 2]
print(sol.better(arr))
print(sol.optimal(arr))