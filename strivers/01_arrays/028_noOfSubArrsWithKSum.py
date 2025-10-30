def noOfSubArrsWithKSum(arr, k):
    n = len(arr)
    prefixSum = dict()
    sm = 0
    cnt = 0
    prefixSum[0] = 1
    for num in arr:
        sm += num
        rem = sm - k
        cnt += prefixSum.get(rem, 0)
        prefixSum[sm] = prefixSum.get(sm, 0) + 1
    return cnt

arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
arr = [3, -3, 1, 1, 1]
k = 3
print(noOfSubArrsWithKSum(arr, k))