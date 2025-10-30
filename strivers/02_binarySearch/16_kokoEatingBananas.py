# Given an array representing piles of bananas, each element - no. of bananas in a pile
# k - rate of eating bananas by koko. k bananas/hr
# koko shouldn't start with next pile as soon as finished with one pile if there is still time to reach an hour
# i.e. if k = 2 bananas/hr and a pile has 3 bananas, technically it would take 1.5 hrs for koko,
# but koko should wait for 0.5 hr to start with next pile. So it would take 2 hrs for koko with k = 2
# Given a time limit in hours for koko to eat all of the piles of bananas, h, find the minimum possible k
def kokoEatingBananas(piles, h):
    '''
    Intuition:
    First of all, we need to find the possible range of k
    Obviously it starts at 1
    The minimum time koko can take to complete a pile is 1 hr
    For koko to complete all piles in 1hr for each, k should be max(piles)
    so the possible range for k is 1 to max(piles)
    Now that, we have a range of answers, we can apply binary search to find our minimum answer
    '''
    def totalHours(hourlyRate):
        # gives the ceil value
        ans = 0
        for pile in piles:
            ans += pile // hourlyRate
            if pile % hourlyRate != 0:
                ans += 1
        return ans
    
    low = 1
    high = max(piles)
    while low <= high:
        mid = low + ((high - low) // 2)
        totHrs = totalHours(mid)
        if totHrs <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low
    '''
    Reason for returning low instead of maintaining a minimum field and updating it with mids:
    - low starts at lowest not an answer
    - high starts at highest possible answer

    - low approaches toward becoming a possible answer
    - high approaches toward becoming not an answer
    Each approaching their polar opposites

    At some point when they crossed over,
    - low would have become the lowest possible answer
    - high would have become the highest not an answer
    '''


piles = [3, 6, 7, 11]
h = 8
print(kokoEatingBananas(piles, h))
# ans = 4 bananas/hr
'''
3 - 1 hr
6 - 2 hrs
7 - 2 hrs
11 - 3 hrs
total - 8 hrs
'''