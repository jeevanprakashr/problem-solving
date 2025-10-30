# given a string, return all possible partitionings where each partition is a palidrome
# possible partitions of "aabb"
# 1 partition = ["aabb"]
# 2 partitions = ["a", "abb"], ["aa", "bb"], ["aab", "b"]
# 3 partitions = ["a", "a", "bb"], ["a", "ab", "b"], ["aa", "b", "b"]
# 4 paritions = ["a", "a", "b", "b"]
# Among these, ["aa", "bb"], ["a", "a", "bb"], ["aa", "b", "b"], ["a", "a", "b", "b"] are the answer as every partition in them are palindromes

def palidromePartitioning(s):
    '''
    Place one partition at a time and check whether the first part of the partition made is a palindrome
    if it is, repeat the same for the part after the placed partition
    if not, move the partition to the next place and check the condition again
    breakpoint is when a partition has been placed at the end of the string
    - aabb
        - "a" | abb  ->  "a" is palindrome, go for abb
            - a | "a" | bb  ->  "a" is palidrome, go for bb
                - a | a | "b" | b  ->  "b" is palidrome, go for b
                    - a | a | b | "b" |  ->  "b" is palidrome, partition is at the end, so its an answer and return
                - a | a | "bb" |  ->  "bb" is palindrom and partition is at the end, so its an answer and return
            - a | "ab" | b  ->  "ab" is not a palidrome, skip
            - a | "abb" |  ->  "abb" is not a palidrome, skip
        - "aa" | bb  ->  "aa" is palidrome, go for bb
            - aa | "b" | b  ->  "b" is palidrome go for b
                - aa | b | "b" |  ->  "b" is palidrome and partition is at the end, so its an answer and return
            - aa | "bb" |  ->  "bb" is palidrome and partition is at the end, so its an answer and return
        - "aab" | b  ->  "aab" is not a palindrome, skip
        - "aabb" |  ->  "aabb" is not a palindrome, skip
    '''
    res = []
    collectPartitionings(0, s, [], res)
    return res

def collectPartitionings(idx, s, path, res):
    '''
    idx - index where the first partition of the current recursion level starts
    s - string
    path - accumulated partitions of the current partitioning path so far
    res - list of answer partitionings
    '''
    if idx == len(s):
        res.append(list(path))
        return
    for i in range(idx, len(s)):
        if isPalindrome(s, idx, i):
            path.append(s[idx:i + 1])
            collectPartitionings(i + 1, s, path, res)
            path.pop()

def isPalindrome(s, start, end):
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

s = "aabb"
print(palidromePartitioning(s))