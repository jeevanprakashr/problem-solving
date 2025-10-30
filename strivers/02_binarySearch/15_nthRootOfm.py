def power(m, n):
    # m^n
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * m
            n = n - 1
        else:
            m = m * m
            n = n // 2
    return ans

def power_optimized(mid, n, m):
    # mid ^ n until m
    '''
    cases will fail if we blindly use above power function because
    what if m is 10^9 and n is 10? we would be trying to find 10^90 which will cause overflow for sure
    this function does the thing which we need simply by doing the following
    return 1 if pwr_ans == m
    return 0 if pwr_ans < m
    return 2 if pwr_ans > m
    '''
    ans = 1
    for i in range(n):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0

def nthRootOfm(n, m):
    low = 1
    high = m
    while low <= high:
        mid = low + ((high - low) // 2)
        pwr_res = power_optimized(mid, n, m)
        if pwr_res == 1:
            return mid
        if pwr_res == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(nthRootOfm(3, 27))
print(nthRootOfm(4, 81))
print(nthRootOfm(4, 69))