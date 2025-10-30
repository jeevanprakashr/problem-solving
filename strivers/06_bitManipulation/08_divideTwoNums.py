# divide two numbers without multiplication or division
def divide(dividend, divisor):
    '''
    Lets take an example of 22/3
    the answer is 7 (not with decimels)
    the brute force can be like
        if we keep removing 3 again and again from 22 until a 3 can't be removed, we can count the no. of times and it will be answer
        but if divisor is 1 and max value of divendend is 2^-31 to (2^31) - 1 (range of integer)
        so it will be O(2^31)
    3 x 7 = 22
    we know that any number can be written in powers of 2
    => 3 x (2^2 + 2^1 + 2^0)
        = (3 x 2^2) + (3 x 2^1) + (3 x 2^0)
        = (3 x 4) + (3 x 2) + (3 x 1)
    from this we can remove 3's in groups of powers of 2
    itr1:
        n = 22
        3 x 1 = 3 < 22
        3 x 2 = 6 < 22
        3 x 4 = 12 < 22
        3 x 8 > 22
        so we can remove four 3s now, i.e.,
        n = 22 - 12 = 10
    itr 2:
        n = 10
        3 x 1 = 3 < 10
        3 x 2 = 6 < 10
        3 x 4 = 12 > 10
        so we can remove two 3s now
        n = 10 - 6 = 4
    itr 3:
        n = 4
        3 x 1 = 3 < 4
        3 x 2 = 6 > 4
        so we can remove one 3 now
        n = 4 - 3 = 1
        since 1 is less than 3, won't go for next iteration
    
    if we add 4 + 2 + 1, we get 7, our answer
    to get powers of 2 with 3, we can use left shift on 3 (this is what we call exponential)
    3 << 0 = 3          1 << 0 = 1
    3 << 1 = 6          1 << 1 = 2
    3 << 2 = 12         1 << 2 = 4
    3 << 3 = 24         1 << 3 = 8
    '''
    if dividend == divisor:
        return 1
    sign = True
    if dividend >= 0 and divisor < 0:
        sign = False
    if dividend < 0 and divisor > 0:
        sign = False
    n = abs(dividend)   # better to store both it in long if used other language
    d = abs(divisor)
    quotient = 0
    while n >= d:
        cnt = 0
        while n >= d << (cnt + 1):  # n >= d * (2**(cnt + 1))       # n >= d x (2^(cnt + 1))
            cnt += 1
        quotient += 1 << cnt  # adding power of 2 (how many d's we removed) # q += 2**cnt
        n -= d << cnt   # n -= d x (2^cnt)
    '''
    # overflow case
    if quotient == 1 << 31 && sign:             # quotient == 2 ^ 31
        return INT_MAX
    if quotient == 1 << 31 && !sign:
        return INT_MIN
    '''
    if sign:
        return quotient
    return -quotient

n = 22
d = 3
print(divide(n, d))