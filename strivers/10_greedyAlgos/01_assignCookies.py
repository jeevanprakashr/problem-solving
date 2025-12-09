# given two arrays of numbers, greed array and cookies array
# greed arr - n children, each with a greed factor greed[i]
# cookies arr - m cookie packets, each with some no. of cookies
# a child with greed factor k can only be satisfied with a cookie packet containing >= k no. of cookies
# a cookie packet can be assigned to only one children wholly
# return the maximum no. of children who can be satisfied with the given cookie packets

def assignCookies(greed, cookies):
    '''
    since we need maximize the no. of satisfied children, we try to give each children only the least satisifiable cookies
    we sort both the array and have two pointers at the start of both sorted array
    we try to map cookies to each child. if a cookie packet can't be mapped, we simply move the cookie pointer to next
    if a child is satisfied, we move the child pointer
    if any one of the pointer moves beyond their array, we return how many children we have crossed.
    '''
    n = len(greed)
    m = len(cookies)
    l = 0
    r = 0
    greed.sort()
    cookies.sort()
    while l < n and r < m:
        if greed[l] <= cookies[r]:
            l += 1
        r += 1
    return l

greed = [1, 5, 3, 3, 4]
cookies = [4, 2, 1, 2, 1, 3]
print(assignCookies(greed, cookies))