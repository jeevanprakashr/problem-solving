# Given n gas stations' coordinates and k gas stations,
# place gas stations such that the max distance between any two gas stations is the minumum
# answers within 10^-6 is acceptable, i.e., decimal answers upto 6 decimal points are allowed
# 0.123456  =>   123456 * 10^-6
# coordinates are sorted
# given gas stations can share coordinates and k gas stations can also be placed in the same coordinate
# Eg: [1, 1, 1, 1], k = 4  =>  place all 4 at 1 itself so that ans remains 0
class MinMaxGasStationsDistance:
    def brute(self, arr, k):
        '''
        Logic:
        arr = [1, 7]  k = 2
        distance between 1 and 7 = 6
        have 2 stations to divide this 6 into 3 equal parts like 2, 2, 2
        so ans is 2

        Eg:
        [1, 13, 17, 23]   k = 5
        sector 1  -->  1 to 13
            distance = 12
        sector 2  -->  13 to 17
            distance = 4
        sector 3  -->  17 to 23
            distance = 6

        sector vs max distance within them
        sector 1  -->  12   gas stations = 0
        sector 2  -->  4    gas stations = 0
        sector 3  -->  6    gas stations = 0

        station 1:
            choose the sector with maximum distance within them to minimize
            chosen = sector 1  (max distance = 12)
            1 gas station in sector 1 divides 12 into 2 parts
            12 / 2 = 6
            distance becomes 12  =>  6, 6
                sector 1  -->  6    gas stations = 1
                sector 2  -->  4    gas stations = 0
                sector 3  -->  6    gas stations = 0
        station 2:
            chosen = sector 3  (max distance = 6)
            gas stations of sector 3 = 1
            => 6 / 2 = 3
            distance becomes 6  =>  3, 3
                sector 1  -->  6    gas stations = 1
                sector 2  -->  4    gas stations = 0
                sector 3  -->  3    gas stations = 1
        station 3:
            chosen = sector 1  (max distance = 6)
            gas stations of sector 1 = 1 + 1 = 2
            => 12 / 3 = 4
            distance becomes 12  =>  4, 4, 4
                sector 1  -->  4    gas stations = 2
                sector 2  -->  4    gas stations = 0
                sector 3  -->  3    gas stations = 1
        station 4:
            chosen = sector 1  (max distance = 4)
            gas stations of sector 1 = 2 + 1 = 3
            => 12 / 4 = 3
            distance becomes 12  =>  3, 3, 3, 3
                sector 1  -->  3    gas stations = 3
                sector 2  -->  4    gas stations = 0
                sector 3  -->  3    gas stations = 1
        station 5:
            chosen = sector 2  (max distance = 4)
            gas stations of sector 2 = 0 + 1 = 1
            => 4 / 2 = 2
            distance becomes 4  =>  2, 2
                sector 1  -->  3    gas stations = 3
                sector 2  -->  2    gas stations = 1
                sector 3  -->  3    gas stations = 1

        max of the max distances within the sectors is 3
        max(3, 2, 3) = 3
        3 is the answer 
        '''
        n = len(arr)
        gasStationsAlloc = [0 for i in range(n - 1)]    # no. gas stations allocated to n - 1 sectors
        for gasStation in range(k):
            maxSectionDist = -1
            maxSector = -1
            for i in range(n - 1):
                sectorDist = arr[i + 1] - arr[i]
                sectionDist = sectorDist / (gasStationsAlloc[i] + 1)
                if maxSectionDist < sectionDist:
                    maxSectionDist = sectionDist
                    maxSector = i
            gasStationsAlloc[maxSector] += 1
        
        maxSectionDist = -1
        for i in range(n - 1):
            sectorDist = arr[i + 1] - arr[i]
            sectionDist = sectorDist / (gasStationsAlloc[i] + 1)
            maxSectionDist = max(maxSectionDist, sectionDist)
        return maxSectionDist
    
    def better(self, arr, k):
        '''
        We have a data struction called Priority queue (availale in Java) which uses heap underneath it
        push and pop takes log(n) and pops the max
        Our example:
        [1, 13, 17, 23]
        gasStationsAlloc = [0, 0, 0]
                            0  1  2    (3 sectors)
        sectionDistances = [12, 6, 4]
        push initial (sectionDist, sector) into priority queue with priority to sectionDist
        pq = [(12, 0), (6, 1), (4, 2)]
        each pop will give the max sectionDist pair
        pop -> update sectionDist  ->  push    for each gas station
        track gasStationsAlloc along with it to update sectionDist
        after all gas stations over pop and get the minimized max sectionDist

        note: in priority queue if 1st element of the pair matches, it goes for the 2nd in the pair to pick the maximum
        '''
    
    def optimal(self, arr, k):
        '''
        obviously the sol in binary search
        range:
        low = 0  =>  Eg: [1, 1, 1, 1] and k = 4  =>  placing all stations at 1 itself
        high = max distance in the given arr so that we can minimize it

        so far we followed a bs template like
        while (low <= high):
            mid = (low + high) // 2
            if (condition(mid)):
                high = mid - 1
            else:
                low = mid + 1
        
        but since answer with upto 10^-6 decimals is accepted here, this won't work
        because the sequence isn't like 0, 1, 2, 3, 4, 5, .... anymore
        it is 0, 0.000001, 0.000002, 0.000003, ....

        so we have change the template like following
        while (high - low > 10^-6):
            mid = (low + high) / 2.0
            if (condition(mid)):
                high = mid
            else:
                low = mid
        
        remember that the opposite polarity concept won't work here as we don't increment or decrement mid with 1. so high is the answer here
        '''
        def noOfStationsRequired(maxDistanceAllowed):
            cnt = 0
            for i in range(1, n):
                sectorDist = arr[i] - arr[i - 1]
                '''
                arr = [1, 2, 3, 4]
                if maxDistanceAllowed = 0.4
                sector 1 = 1, 1.4, 1.8, 2    =>   maxDist = 0.4
                sector 2 = 2, 2.4, 2.8, 3    =>   maxDist = 0.4
                so 2 gas stations can be placed in sector 1
                =>  1 / 0.4 = 2.5 ~= 2   =>   that's why sectorDist is divided with '//' which gives stations required

                but if maxDistanceAllowed = 0.5
                =>  1 / 0.5 = 2
                but 1 station is enough to get maxDist = 0.5
                thats why the condition -> if maxDistanceAllowed equally splits the distance
                '''
                sections = sectorDist // maxDistanceAllowed
                stationsCnt = sections
                if sectorDist == sections * maxDistanceAllowed:
                    stationsCnt -= 1
                cnt += stationsCnt
            return cnt
        
        n = len(arr)
        low = 0
        high = 0
        for i in range(1, n):
            high = max(high, arr[i] - arr[i - 1])
        diff = 10**(-6)
        while high - low > diff:
            mid = (low + high) / 2.0
            requiredStations = noOfStationsRequired(mid)
            if requiredStations > k:
                low = mid
            else:
                high = mid
        return high


arr = [1, 13, 17, 23]
k = 5
arr = [1, 2, 3, 4, 5]
k = 4
arr = [1, 1, 1, 1]
k = 4
sol = MinMaxGasStationsDistance()
print(sol.brute(arr, k))
print(sol.optimal(arr, k))

