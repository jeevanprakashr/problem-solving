def noOfSubArrsWithXorK(arr, k):
    # xor - cancel out same nums in pairs
    # Intutition (Same logic used in 018_maxSubArrWithSumK and 028_noOfSubArrsWithKSum)
    # Let xor(arr[0:y]) = xr
    # If there exists a sub array ending at y that gives k xor, i.e xor(arr[x:y]) = k ; x > 0
    # then we need to find the prefix xor which is xor(arr[0:x]) and check whether we saw it
    # let the prefix xor be px, method to find px
    # we know, px ^ k = xr
    # px ^ k ^ k = xr ^ k      ; xor cancels pairs
    # px = xr ^ k      ; check whether we saw px before while traversing arr
    n = len(arr)
    prefixXor = dict()
    xor = 0
    prefixXor[xor] = 1  # we need entry for 0 xor too for cases with sub array starting at 0 as our solution
    cnt = 0
    for i in range(n):
        xor = xor ^ arr[i]
        px = xor ^ k
        cnt += prefixXor.get(px, 0)
        prefixXor[xor] = prefixXor.get(xor, 0) + 1
    return cnt

arr = [4, 2, 2, 6, 4]
k = 6
print(noOfSubArrsWithXorK(arr, k))