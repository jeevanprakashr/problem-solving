# given an string of 'a', 'b' and 'c', return the count of substrings which have all three characters

def noOfSubStrsWithAll3Chars(s):
    '''
    Lets take an example
    s = "bbacba"
    if we use brute force, the solution would be using two loops to generate a substring,
    outer loop for start idx and inner loop for end idx, and count the satisfying substrings.
    i -> 0 to n-1
        hash = [a=0, b=0, c=0]
        j -> i to n-1
            c = s[j]
            hash[c] = 1
            if all chars seen:
                cnt += 1
    we can slightly optimize this brute force with a simple realization
    lets take the valid sub string "bac"
    since "bac" is valid, then adding all the characters following 'c' to the substring will also be valid
    so simply do cnt += n - j and break the inner loop

    we will be using this optimising technique in our optimal solution using window approach
    lets consider looking backward to form a substring instead of looking forward
    
    we can say, for every character, there is a subtring that ends with it.
    our goal is to find the minimal window for every character that contains all three characters and ends with that character

    for example, s = "bbacba"
    for char 'b' at idx 4, the window is "acb" that starts from 2 and ends at 4
    for char 'c' at idx 3, the window is "bac" that starts from 1 and ends at 3

    if s = "bbaccba"
    for char 'c' at idx 4, the window is "bacc" that starts from 2 and ends at 4

    so, if we find this minimal window for every character,
    then we can find the no. of satisfying subarrays that ends with this character from the start of the window
    like cnt += start + 1

    to find the minimal window for every charcter, we track the last seen index for 'a', 'b' and 'c'
    if all of them are set, then we got our window and the start would the minimum of these three values
    
    for example, s = "bbacba"
    for char 'c' at idx 3, the last seen idxs would be
    a = 2, b = 1, c = 3
    here b = 1 is the minumum which is the start of our minimal window
    '''
    lastSeen = [-1, -1, -1]
    n = len(s)
    cnt = 0
    for i in range(n):
        lastSeen[ord(s[i]) - ord('a')] = i
        if min(lastSeen) != -1:
            cnt += 1 + min(lastSeen)
        # the if check is not needed as min(lastSeen) = -1 means cnt += 1 + (-1) which makes no change to cnt
        # only written to understand
    return cnt

s = "bbacba"
print(noOfSubStrsWithAll3Chars(s))