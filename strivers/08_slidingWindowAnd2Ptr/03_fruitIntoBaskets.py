# there are n trees producing limited "types" of fruits in continuous order
# there are two baskets, each basket can be filled with any number of fruits 
# but the fruits should be of same type like
# basket-1 - containes only type-A fruits
# basket-2 - containes only type-C fruits and the combinations go on
# And also trees should be selected only in the continuous order
# can't select tree-1 and jump to tree-4
# can start from anywhere
# return max no. of fruits
'''
format:
    arr of numbers where arr[i] indicates the type of the fruit
    eg: [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    ans would be 5
    [1, 2, 1, 1, 2]
    => b1 - [1, 1, 1]
       b2 - [2, 2]

can also be said as
return max length of subarray with atmost 2 types of numbers
'atmost' - we can have only one fruit in one basket and keep the other basket empty when arr has only one type of numbers
'''
class FruitIntoBasket:
    '''
    lets have k variable telling no. of buckets
    '''
    def better(self, arr, k):
        '''
        keep l and r pointer
        maintain a map of type vs frequency
        move r and note the frequency of the type at r
        if map size exceeds 2 (buckets), move l and decrement the frequency of type at l each type until map size becomes 2
        if frequency of type at l becomes 0, remove it from map
        then again start with r
        keep track of max length of the window each time
        '''
        l = 0
        r = 0
        n = len(arr)
        mp = dict()
        mxLen = 0
        while r < n:
            mp[arr[r]] = mp.get(arr[r], 0) + 1
            while len(mp) > k:
                mp[arr[l]] -= 1
                if mp[arr[l]] == 0:
                    mp.pop(arr[l])
                l += 1
            if len(mp) <= k:
                mxLen = max(mxLen, r - l + 1)
            r += 1
        return mxLen
    
    def optimal(self, arr, k):
        '''
        optimal for the same reason as explained in previous problem 02_mxConsecutive1sWithKFlips
        solution is also the same as previous problem
        '''
        l = 0
        r = 0
        n = len(arr)
        mp = dict()
        mxLen = 0
        while r < n:
            mp[arr[r]] = mp.get(arr[r], 0) + 1
            if len(mp) > k:
                mp[arr[l]] -= 1
                if mp[arr[l]] == 0:
                    mp.pop(arr[l])
                l += 1
            if len(mp) <= k:
                mxLen = max(mxLen, r - l + 1)
            r += 1
        return mxLen
    
arr = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
k = 2
sol = FruitIntoBasket()
print(sol.better(arr, k))
print(sol.optimal(arr, k))