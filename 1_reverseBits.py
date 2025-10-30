# https://www.naukri.com/code360/problems/reverse-bits_2181102?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

def int2bin(n):
    res = 0
    cnt = 0
    while n > 0:
        digit = n % 2
        res += digit * (10**cnt)
        cnt += 1
        n //= 2
    return res

def bin2int(n):
    res = 0
    cnt = 0
    while n > 0:
        digit = n % 10
        res += digit * (2**cnt)
        cnt += 1
        n //= 10
    return res

def reverseBits(n):
    binary = int2bin(n)
    revBinary = 0
    cnt = 0
    while binary > 0:
        digit = binary % 10
        revBinary = (revBinary * 10) + digit
        binary //= 10
        cnt += 1
    revBinary = revBinary * (10**(32 - cnt))
    return bin2int(revBinary)

print(reverseBits(12))