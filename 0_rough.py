def checkArmstrong(n):
    sm = 0
    dup = n
    while n > 0:
        digit = n % 10
        sm += digit**3
        n //= 10
    return sm == dup

print(checkArmstrong(1634))