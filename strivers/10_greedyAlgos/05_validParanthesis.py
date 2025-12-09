# given a string of characters '(', ')' and '*'
# '*' can be substituted with '(' or ')' or an empty character
# return if it is possible for the paranthesis string to be valid with or without the help of '*'
class ValidParanthesis:
    def brute(self, s):
        '''
        the brute approach is to try every possibility for a '*'
        first need a approach to determine if a normal paranthesis without '*' is valid
        since it would only has '(' and ')', a simple counter (gauge) will do.
        
        start the counter from 0
        for every '(', increment the counter
        for every ')', decrement it.
        At the end, if the counter remains 0, then the string is valid
        There is an edge case. What if s = "())("
        it would also make counter to 0 according to our approach.
        so whenever the counter goes negative, then and there return the string is invalid

        now back to our original solution
        we use recursion to try all the three possible ways to replace '*' when we encounter one
        when any one of the pathway of the recursion tree returns true, the we can achieve a valid string
        TC: N^3
        SC: N
        '''
        def isValid(s, n, idx, cnt):
            if cnt < 0:
                return False
            if idx == n:
                return cnt == 0
            if s[idx] == '(':
                return isValid(s, n, idx + 1, cnt + 1)
            if s[idx] == ')':
                return isValid(s, n, idx + 1, cnt - 1)
            else:
                return isValid(s, n, idx + 1, cnt + 1) or isValid(s, n, idx + 1, cnt) or isValid(s, n, idx + 1, cnt - 1)
        
        n = len(s)
        return isValid(s, n, 0, 0)
    
    '''
    better approach is using DP with memoisation. we have index and counter both ranging form 0 to n. so use n x n matrix
    to memoise the outcome the isValid function
    TC: n^2
    sc = n^2
    '''

    def optimal(self, s):
        '''
        when '*' is encounter, there are 3 ways the counter can change
        -1, 0 or +1
        this is a range -1 to +1

        for eg. if s = "*" the range for cnt is [-1, 1]
        and 0 is within this range. so 0 can be achieved and is valid

        with this in mind we maintain two counters
        min - lower bound of the range
        max - upper bound of the range
        for every character we re evaluate our min, max range
        ofcourse if a possiblity causes to go negative, we ignore going that way

        eg:
        s = "()*)*()"
        char    min     max     remarks
        (       1       1       only one possiblity for '(', incr the counter
        )       0       0       ')' - decr the counter
        *       0       1       min = 0 => can be -1, 0, 1
                                           -1 is out of the question as it causes negative
                                           so 0 is the lower bound
                                max = 0 => can be -1, 0, 1
                                           -1 - ignore as it is negative
                                           remaining - 0 and 1 out of which 1 is the max and chosen as upper bound
        )       0       0       min = 0 => ')' causes negative -1, prune the negative part and move the lower bound back to 0
                                max = 1 => decrement to 0
        *       0       1       same as before as first '*'
        (       1       2       '(' - increment
        )       0       1       ')' - decrement

        our final range is [0, 1] after covering all possiblities which has 0 in it. so this string is valid

        s = "(**("
        char    min     max     remarks
        (       1       1
        *       0       2       min = 1 => can be 0, 1, 2
                                           so 0 is the lower bound
                                max = 1 => can be 0, 1, 2
                                           2 is the max and hence the upper bound
                                so our range now has (0, 1, 2)
        *       0       3       min = 0 => can be -1, 0, 1
                                           -1 - pruned
                                           so 0 stays as our lower bound
                                max = 2 => can be 1, 2, 3
                                           3 is the max and hence our upper bound
                                so our range now has (0, 1, 2, 3)
        (       1       4       '(' - increment
        the final range is [1, 4] and 0 is not within them. so the string can't be made as valid

        this solution too considers all the possible ways but try to incorporate them within a range
        if 0 is within that range, then it can be attained

        there is an edge case for max
        we say if min goes below 0, we simply prune negative and make it as 0
        but if max goes negative, for e.g, if the s starts with ')', then max will be -1
        if max itself becomes negative, then it is impossible to maintain the range and hence return 0
        
        after iterating all the chars, simply check if min == 0
        '''
        mn = 0
        mx = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                mn += 1
                mx += 1
            elif s[i] == ')':
                mn -= 1
                mx -= 1
            else:
                mn -= 1
                mx += 1
            if mn < 0:
                mn = 0
            if mx < 0:
                return False
        return mn == 0
    
s = "()*)*()"
sol = ValidParanthesis()
print(sol.brute(s))
print(sol.optimal(s))