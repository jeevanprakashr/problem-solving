# given a value v and an abundance of coins with denominations 1, 2, 5, 10, 20, 50, 100, 500, 1000
# return the minimum number of coins needed to make up the value v in total
# sample v = 49
# the solution is 20, 20, 5, 2, 2 = 49
# the no. of coins is 5 which is our answer

def minNoOfCoins(v):
    '''
    if we greedily pick the closest lower or equal denomination and subtract it with our v until we reach 0,
    we can find our minimum no of coins

    the algo is simple
    start from the end the of denominations array
    until the current denom is less than or equal to the remaining value of v, keep subtracting it from v
    once the value becomes less than the denom, move to the lesser denom

    eg:
    v = 49
    denoms = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    denom   v   remarks
    1000    49  greater

    500     49  greater

    100     49  greater

    50      49  greater

    20      49  lesser
            29  lesser
            9   greater

    5       9   lesser
            4   greater
    
    2       4   lesser
            2   lesser
            0   greater

    1       0   greater

    info:
    if denoms are like [1, 5, 6, 9]
    and v = 11
    according to our greedy algo the coins would be [9, 1, 1] which would be 3 coins
    but we can achieve 11 from [5, 6] itself which are only 2 coins
    the reason our greedy algo fails here is because of the constitution of denoms

    our original denoms are designed in a way that if you add any two consecution denoms, it wouldn't greater than than the next third denom
    but in [1, 5, 6, 9], 5 + 6 = 11 > 9
    this is the reason the greedy algo fails here.
    This design of denoms is true in reality.
    '''
    denoms = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    ans = []
    total = 0
    for i in range(len(denoms) - 1, -1, -1):
        while denoms[i] <= v:
            v -= denoms[i]
            ans.append(denoms[i])
            total += 1
    return ans, total

print(minNoOfCoins(49))