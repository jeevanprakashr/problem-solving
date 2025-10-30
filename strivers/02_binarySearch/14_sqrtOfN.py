def sqrt(n):
    low = 1
    high = n
    while low <= high:
        mid = low + ((high - low) // 2)
        if mid * mid <= n:
            low = mid + 1
        else:
            high = mid - 1
    return high

print(sqrt(28))