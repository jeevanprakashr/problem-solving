# given an arr of first n natural numbers with a missing number and a number repeating twice. Return in order of [repeating, missing]
class FindMissingAndRepeatingNum:
    def solutionOne(self, arr):
        '''
        uses plain maths equation solving
        lets arr = [a, b, c, x, x, z] and n natural nums = [a, b, c, x, y, z]
        sum(arr) - sum(nat) = s1        # sum(nat) = (n * (n + 1)) / 2
        => x - y = s1 ----> (1)

        lets do squares now
        sum(arr_squares) - sum(nat_squares) = s2       # sum(nat_squares) = (n * (n + 1) * (2 * n + 1)) / 6
        => x2 - y2 = s2
           (x + y)(x - y) = s2
           x + y = s2 / s1 = s3
           x + y = s3 -----> (2)
        
        (1) + (2)  =>  2x = s1 + s3
                        x = (s1 + s3) / 2
        => y = x - s1
        now we have found both x and y
        x - repeating
        y - missing
        '''
        n = len(arr)
        sn = (n * (n + 1)) // 2     # sum(nat)
        s2n = (n * (n + 1) * (2 * n + 1)) // 6      # sum(nat_squares)
        s = 0
        s2 = 0
        for i in range(n):
            s += arr[i]
            s2 += arr[i] * arr[i]
        val1 = s - sn
        val2 = s2 - s2n
        val2 = val2 // val1
        x = (val1 + val2) // 2
        y = x - val1
        return [x, y]
    
    def solutionTwo(self, arr):
        '''
        uses xor method
        xor - cancel out pairs
        lets find xor(arr) and xor(nat) and xor them
        xor(arr) ^ xor(nat) = x1     # cancels all the pairs
        => x ^ y = x1
        when xor-ing 2 diff nums, atleast one bit will be different between them, lets find the right most diff bit
        lets say x = 1 and y = 5
        x1 = 4
        1 = 001
        5 = 101
        diffBit = 2   # 2nd right most 'index'

        method to find diffbit
        - and-ing x1 with left-shifted '1'
        x1 = 4 = 100
        100 & 001 = 0
        1 << 1  =>  100 & 010 = 0
        1 << 2  =>  100 & 100 = 1 != 0, hence diffBit = 2

        now lets group arr and nat into two groups,
        zero club = having 2nd bit as 0
        one club = having 2nd bit as 1
        one of these two clubs will have a number occuring three times and other one will have a number occuring only one time
        if we do xor of these clubs, we will get x and y.
        still we won't know which one is repeating and which one is missing, so verify them with the given arr

        method to find 0 or 1 as 2nd bit
        lets say z = 4
        z & (1 << diffBit)
        4 & (1 << 2) = 100 & 100 = 1  -->  one club
        if z = 2,
        010 & 100 = 0  -->  zero club
        '''
        n = len(arr)
        xr = 0
        for i in range(n):
            xr = xr ^ arr[i]
            xr = xr ^ (i + 1)
        diffBit = 0
        while True:
            if xr & (1 << diffBit) != 0:
                break
            diffBit += 1
        # easy bit manipulationt trick to find 1 << diffBit without calculation diffBit
        # xr & ~(xr - 1)
        # 1 << diffBit = xr & ~(xr - 1)
        zero = 0
        one = 0
        for i in range(n):
            if arr[i] & (1 << diffBit) != 0:
                one = one ^ arr[i]
            else:
                zero = zero ^ arr[i]
            
            if (i + 1) & (1 << diffBit) != 0:
                one = one ^ (i + 1)
            else:
                zero = zero ^ (i + 1)
        
        cnt = 0
        for i in range(n):
            if arr[i] == zero:
                cnt += 1
        if cnt == 2:
            return [zero, one]
        return [one, zero]

arr = [4, 3, 6, 2, 1, 1]
sol = FindMissingAndRepeatingNum()
print(sol.solutionOne(arr))
print(sol.solutionTwo(arr))