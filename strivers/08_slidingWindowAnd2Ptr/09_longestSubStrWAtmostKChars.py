# given a string and k, return the longest substring with atmost k distinct characters
# sample: s = "aaabbccd"    k = 2
# "aaabb", "aaa", "d" are satisfying substrings but "aaabbc" is not as it contains 3 distinct characters

def longestSubStrWAtmostKChars(s, k):
    '''
    gonna use sliding window template as we saw in our previous problems
    move r pointer and calcuate length of the window and thereby updating maxlen
    whenever the condition for the window breaks, move the l pointer by only one step which is enough
    no need to move l pointer all the way till the condition satisfies as our goal is only to maximize the size of the window
    if the window eventually satisifies at some point, we can update our maxlen
    then move r pointer as usual.
    '''
    n = len(s)
    mpp = dict()
    l = 0
    r = 0
    maxLen = 0
    while r < n:
        mpp[s[r]] = mpp.get(s[r], 0) + 1
        if len(mpp) > k:
            mpp[s[l]] -= 1
            if mpp[s[l]] == 0:
                mpp.pop(s[l])
            l += 1
        if len(mpp) <= k:
            maxLen = max(maxLen, r - l + 1)
        r += 1
    return maxLen

s = "aaabbccd"
k = 2
print(longestSubStrWAtmostKChars(s, k))
