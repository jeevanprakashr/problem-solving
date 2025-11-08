# given a string and a number k, return longest substring length containing a single repeating character
# after replacing atmost k characters if needed

class LongestRepCharsWithKReplaces:
    def better(self, s, k):
        '''
        we already know the solution is sliding window since this is a question of substring
        the biggest question here is how we know which characters to replace and with which character we replace them
        the answer is greedy and simple
        we replace the characters which has less frequency and replace them with the character with max frequency in the window
        lets take "AABAB" and k is 2
        here freq(A) = 3 and freq(B) = 2
        its obvious we need to replace B with A here
        and to check the validity of the window size we can say
        window length - max frequency <= k 
        so that the lower frequency characters can be replaced
        to track the frequency, we use map and track max frequency too
        when this condition breaks, we shrink the window thereby recalculating frequency and max frequency
        '''
        n = len(s)
        mp = dict()
        l = 0
        r = 0
        mxFreq = 0
        mxLen = 0
        while r < n:
            mp[s[r]] = mp.get(s[r], 0) + 1
            mxFreq = max(mxFreq, mp[s[r]])
            while (r - l + 1) - mxFreq > k:
                mp[s[l]] -= 1
                for char in mp:
                    mxFreq = max(mxFreq, mp[char])
                l += 1
            if (r - l + 1) - mxFreq <= k:
                mxLen = max(mxLen, r - l + 1)
            r += 1
        return mxLen
    
    def optimal(self, s, k):
        '''
        Lets optimize the re calculation of max frequency
        the recalculation itself is not needed
        lets take "AAABB" in "AAABBCCD" and k is 2
        here mxfreq = 3
        so 5 - 3 = 2 <= 2
        when going to 'C', this condition breaks and we starts shrinking
        and the only impact the shrinking can possibly do is decrease the maxFreq which increase the no. of chars to be replaced
        but out goal is make it stay below k and to maximize our window length
        if 5 becomes 6, then making 3 to 2 doesn't actually gives any change to our result
        we only need 3 to increase so that we stay within k range
        
        and as for shrinking, we can avoid that too as we saw in the previous problems
        '''
        n = len(s)
        mp = dict()
        l = 0
        r = 0
        mxFreq = 0
        mxLen = 0
        while r < n:
            mp[s[r]] = mp.get(s[r], 0) + 1
            mxFreq = max(mxFreq, mp[s[r]])
            if (r - l + 1) - mxFreq > k:
                mp[s[l]] -= 1
                l += 1
            if (r - l + 1) - mxFreq <= k:
                mxLen = max(mxLen, r - l + 1)
            r += 1
        return mxLen

s = "AABABBA"
s = "AAABBCCD"
k = 2
sol = LongestRepCharsWithKReplaces()
print(sol.better(s, k))