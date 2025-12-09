# given a list of pairs of numbers
# each pair represents an item
# first value of pair - value of the item
# second value of pair - weight of the item
# also given a value w
# w - maximum weight that can be stored in the sack
# select items to be filled in the sack whose total weight satisfies w
# goal is to find the maximum total value of the items that can be filled in the sack
# selecting a fraction / part of an item is allowed and respective weight and value should calculated
# sample: [(100, 20), (60, 10), (100, 50), (200, 50)]   w = 90
# ans = 380
# picked (100, 20), (60, 10), (200, 50) which makes up 80 in weight and we have 10 more to fill
# we find value per weight unit in (100, 50) and calculate value for weight 10 which is 20
# to total = 100 + 60 + 200 + 20 = 380

def fractionalKnapsack(itemPairs, w):
    '''
    we find value per weight unit for all items and choose items greedily from larger to smaller values of per unit weight
    by sorting the pairs based on value per unit weight
    '''
    itemPairs.sort(key = lambda pair: pair[0] / pair[1], reverse = True)
    totalVal = 0
    for i in range(len(itemPairs)):
        if itemPairs[i][1] <= w:
            totalVal += itemPairs[i][0]
            w -= itemPairs[i][1]
        else:
            totalVal += (itemPairs[i][0] / itemPairs[i][1]) * w
            break
    return totalVal

itemPairs = [(100, 20), (60, 10), (100, 50), (200, 50)]
w = 90
print(fractionalKnapsack(itemPairs, w))