# you are running a lemonade stall selling a lemonade for 5 rs.
# at first, there is no change (money)
# there are n customers with 3 types of bill which are ₹5, ₹10 and ₹20
# each customer should be sold with a lemonade
# return if it possible or not to sell to all the customers
# sample:
'''
bills = [5, 5, 5, 10, 20]
bill    ₹5      ₹10     ₹20     canSell?
5       1       0       0       yes
5       2       0       0       yes
5       3       0       0       yes
10      2       1       0       yes (return a ₹5 change to customer)
20      1       0       1       yes (return a ₹10 and a ₹5 to customer)
ans = True

bills = [5, 5, 10, 10, 20]
bill    ₹5      ₹10     ₹20     canSell?
5       1       0       0       yes
5       2       0       0       yes
10      1       1       0       yes (return a ₹5 change to customer)
10      0       2       0       yes (return a ₹5 change to customer)
20      0       2       0       no (should return ₹15 to the customer by only have 2 ₹10 bills, we need either ₹10 + ₹5 or ₹5 + ₹5 + ₹5)
ans = False
'''

def lemonadeChange(arr):
    '''
    from the problem statement, the solution is simple and straightforward
    there are only 3 situations
    if customer gives
    ₹5  -   simply increment no. of 5s
    ₹10 -   5s - 1,
            10s + 1
    ₹20 -   10s - 1,
            5s - 1
            or
            5s - 3
    no need to track no. of 20s as we won't be giving them to customers as change
    '''
    five = 0
    ten = 0
    for i in range(len(arr)):
        if arr[i] == 5:
            five += 1
        elif arr[i] == 10:
            if five:
                five -= 1
                ten += 1
            else:
                return False
        else:
            if ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True

print(lemonadeChange([5, 5, 5, 10, 20]))
print(lemonadeChange([5, 5, 10, 10, 20]))

