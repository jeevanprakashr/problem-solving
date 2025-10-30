# Given arr of items where arr[i] = weight of item i
# Given d days within which we should carry all the items in a ship
# ship will travel once per day
# find least capacity of the ship needed
'''
Eg: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = 5 days
if capacity = 10
day 1 = [1, 2, 3, 4] = sum is 10
day 2 = [5]
day 3 = [6]
day 4 = [7]
day 5 = [8]
day 6 = [9]
day 7 = [10]
7 days > d
not an answer

if capacity = 15
day 1 = [1, 2, 3, 4, 5]
day 2 = [6, 7]
day 3 = [8]
day 4 = [9]
day 5 = [10]
5 days = d
hence 15 is an answer

if 15 is possible answer then, anything above 15 is also an answer
'''

def leastShipCapToSendItems(weights, days):
    '''
    min answer - 1 day - to get this capacity should be sum of weights - high
    min capacity needed - max of weights to be shipped - low
    '''
    def possible(capacity):
        d = 1
        load = 0
        for i in range(n):
            if load + weights[i] > capacity:
                d += 1
                load = weights[i]
            else:
                load += weights[i]
        return d <= days
    
    n = len(weights)
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = low + ((high - low) // 2)
        if possible(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(leastShipCapToSendItems(weights, days))