# given a string, return the length of the longest substring without repeating characters

def longestSubStrWoReptChars(s):
    '''
    two pointer approach:
    whenever we encounter a problem dealing with substring, think of 2 pointer approach with sliding window
    Have two pointers at the start, l and r
    have a map to record chars and last seen index
    move r and register in the map
    if a char is seen and its index is after l, move l to the stored index + 1 and update the new index in the map
    track the max len which r - l + 1 along.
    '''
    n = len(s)
    d = dict()
    l = 0
    r = 0
    mxLen = 0
    ln = 0
    while r < n:
        if s[r] in d and d[s[r]] >= l:
            l = d[s[r]] + 1
        ln = r - l + 1
        mxLen = max(mxLen, ln)
        d[s[r]] = r
        r += 1
    return mxLen

s = "cadbzabcd"
print(longestSubStrWoReptChars(s))
        