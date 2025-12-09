# given n jobs each having different processing times
# return average waiting time a job to get their turn

def shortestJobFirst(jobs):
    '''
    sort the jobs and calculate the waiting time for each job
    '''
    n = len(jobs)
    jobs.sort()
    t = 0
    wtTime = 0
    for i in range(n):
        wtTime += t
        t += jobs[i]
    return wtTime // n

arr = [4, 3, 7, 1, 2]
print(shortestJobFirst(arr))