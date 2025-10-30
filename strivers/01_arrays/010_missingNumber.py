class MissingNumber:
    def methodOne_summation(self, arr, n):
        sm1 = (n * (n + 1)) // 2
        sm2 = 0
        for n in arr:
            sm2 += n
        return sm1 - sm2
    
    def methodTwo_xor(self, arr, n):
        xor1 = 0
        xor2 = 0
        for i in range(n - 1):
            xor1 = xor1 ^ arr[i]
            xor2 = xor2 ^ (i + 1)
        xor2 = xor2 ^ n
        return xor1 ^ xor2

arr = [1, 2, 4, 5]
n = 5
mn = MissingNumber()
print(mn.methodOne_summation(arr, n))
print(mn.methodTwo_xor(arr, n))
