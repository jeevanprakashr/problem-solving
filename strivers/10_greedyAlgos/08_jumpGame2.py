# the problem statement is the same as the previous one, 07_jumpGame
# but here there would be no 0's in the array, which means it is sure to reach the end
# now the goal is to return minimum no. of jumps needed to reach the end

class JumpGame2:
    def brute(self, arr):
        '''
        the bruteforce appoach is to try every possible ways to reach the end.
        When it comes to try every possible combinations, the solution is using recursive approach
        the break condtion for the recursive way is if we stand at the last index, we return the accumulated jumps
        else if we repeat the same for all possible jumps from the current index and return minimum of those results
        '''
        def recursiveJumps(idx, jumps):
            if idx >= n - 1:
                return jumps
            mini = float("inf")
            for i in range(1, arr[idx] + 1):    # no. of steps we can skip. 0 not considered as it would mean that we stay the same step
                mini = min(mini, recursiveJumps(idx + i, jumps + 1))
            return mini
        
        n = len(arr)
        return recursiveJumps(0, 0)
    
    def better(self, arr):
        '''
        the better approach would be using DP with memoisation.
        in the above recursive method, we have two variables, idx and jump both ranging 0 to n - 1
        idx, jump -> nxn matrix -> memoisation
        the TC would reduce from n^n to n^2
        '''
    
    def optimal(self, arr):
        '''
        for optimal approach, we are going to do something as similar as we did in 05_validParanthesis problem,
        which is by using ranges
        lets start with 0 to 0 range at first where 0 is index
        we maintain l and r where l is minimum and r in maximum (farthest one can jump)
        and every time we update the range, we increment our jumps.
        once we reach end, we return no. of jumps.
        lets take an example
        arr = [2, 3, 1, 4, 1, 1, 1, 2]
        idx     num     idx range (l-r)     jumps       remarks
        0       2       1-2                 1           can reach 1 and 2 indices with just 1 jump from 0
        1,2     3,1     3-4                 2           idx 2 can be reached from idx 1 with an additional jump, but we can already reach idx 1 with just 1 jump, so pruning it from range
                                                        indices 3 and 4 can be reached with minimum of 2 jumps
        3,4     4,1     5-7                 3           indices 4 to 7 can be reached with minimum of 3 jumps and we have reached the end
        
        let's think it like this way.
        what we are trying to do is divide the array into continuous ranges.
        the position of a range starting from 1 defines the min no of jumps needed to reach any number within that range.
        by default the starting number will form the first range by itself.
        when in each range, we try to find farthest point one can reach beyond that range.
        that farthest point will become the end of the next range
        and obviously the next element right after the current range will become the start of the next range which is by default the minimum point one can reach "beyond the range", not "within the range" which is waste of time.
        
        think of attack on titan's, they only needed three walls to protect all the humans inside
        and think of they started building from the innermost wall to outwards
        '''
        n = len(arr)
        l = 0
        r = 0
        jumps = 0
        while r < n - 1:    # if r reaches n - 1 then we are at the end of the arr and break the loop
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + arr[i])
            l = r + 1
            r = farthest
            jumps += 1
        return jumps

sol = JumpGame2()
arr = [2, 3, 1, 4, 1, 1, 1, 2]
print(sol.brute(arr))
print(sol.optimal(arr))