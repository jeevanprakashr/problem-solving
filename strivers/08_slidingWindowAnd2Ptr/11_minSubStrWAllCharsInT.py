# given two string s and t, return the minumum length substring that contains all the characters in t
# sample:
# s = "ddaaabbca"     t = "abc"
# ans = "bca"
# even t has duplicate characters, the frequency of characters in t should also be accounted for.
# if t = "abbc" then "bca" is not valid substring string b is occurring only once in the substring

def minSubStrWAllCharsInT(s, t):
    '''
    solution is to use a map and sliding window
    the map would have the frequency of characters in t preloaded before starting sliding window
    whenever a character in the map is encountered while moving r of the window, we decrement the frequency
    we also keep track of how many chars in t have been encountered till now
    when it reaches the length of t, we have a valid substring
    we note the start index and the length to track the minumum length
    since we need minimum, we would shrink the window and increment in the map and decrement the length counter while doing
    '''
    n = len(s)
    m = len(t)
    minLen = float('inf')
    sIndex = -1
    cnt = 0
    l = 0
    r = 0
    mpp = dict()
    for c in t:
        mpp[c] = mpp.get(c, 0) + 1
    while r < n:
        if s[r] in mpp:
            if mpp[s[r]] > 0:
                cnt += 1
            mpp[s[r]] -= 1
        while cnt == m:
            if r - l + 1 < minLen:
                minLen = r - l + 1
                sIndex = l
            if s[l] in mpp:
                mpp[s[l]] += 1
                if mpp[s[l]] > 0:
                    cnt -= 1
            l += 1
        r += 1
    if sIndex == -1:
        return ""
    return s[sIndex:sIndex + minLen]

s = "ddaaabbca"
t = "abc"
print(minSubStrWAllCharsInT(s, t))
