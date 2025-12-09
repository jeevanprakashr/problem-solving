# given n jobs, each job have an id, deadline - last day to complete the job, and profit
# on a day, only one job can be done and each job can be done in a day
# if the day passes beyond the deadline of a job, that job can't be done
# return the maximum profit that can be gained
# sample:
# id    deadline    profit
# 1     4           40
# 2     1           10
# 3     1           40
# 4     1           30
# the job 1 can be done on days 1, 2, 3 and 4 but not on 5 and after
# so by choosing jobs like
# day   job     profit
# 1     3       40
# 2     1       40
# the res is 80

def jobSequencingProblem(jobs):
    '''
    a job can be done on the last day and we must prioritize the larger profit jobs to maximize our result.
    with this logic, we will first sort the jobs based on profit in descending order
    and for each job, we will allocate it to the last day of the deadline using a hash. if it is not available, then we can check on previous days
    by this we can get our maximum profit.

    lets take an example
    jobs = [
        (1, 4, 20),
        (2, 5, 60),
        (3, 6, 70),
        (4, 6, 65),
        (5, 4, 25),
        (6, 2, 80),
        (7, 2, 10),
        (8, 2, 22)
    ]
    job -> (id, deadline, profit)
    we see that the max deadline is 6 which means we can only do 6 jobs and only in 6 days not beyond that
    so lets form an hash for 6 days and initialize all the days with -1
    after sorting based on profit
    jobs = [
        (6, 2, 80),
        (3, 6, 70),
        (4, 6, 65),
        (2, 5, 60),
        (5, 4, 25),
        (8, 2, 22)
        (1, 4, 20),
        (7, 2, 10),
    ]
    lets iterate
    job     deadline        hash                        profit      remarks
    6       2               [-1, 6, -1, -1, -1, -1]     80          since deadline is 2, we can do it on the last day which is 2, hence day 2 is taken in the hash
    3       6               [-1, 6, -1, -1, -1, 3]      70
    4       6               [-1, 6, -1, -1, 4, 3]       65          since 6 is already taken by job-3, we can do job-4 on day-5, hence day-5 is taken
    2       5               [-1, 6, -1, 2, 4, 3]        60          since day-5 is taken, taking day-4
    5       4               [-1, 6, 5, 2, 4, 3]         25          since day-4 is taken, taking day-3
    8       2               [8, 6, 5, 2, 4, 3]          22          since day-2 is taken, taking day-1
    total profit is our maximum profit and total no. of jobs that can be done is 6
    '''
    n = len(jobs)
    jobs.sort(key = lambda job: job[2], reverse = True)
    maxDeadLine = 0
    for i in range(n):
        maxDeadLine = max(maxDeadLine, jobs[i][1])
    hsh = [-1 for i in range(maxDeadLine + 1)]
    totalProfit = 0
    cnt = 0
    for i in range(n):
        jobId = jobs[i][0]
        deadline = jobs[i][1]
        profit = jobs[i][2]
        for j in range(deadline, 0, -1):
            if hsh[j] == -1:
                hsh[j] = jobId
                cnt += 1
                totalProfit += profit
                break
    return cnt, totalProfit



jobs = [
    (1, 4, 20),
    (2, 5, 60),
    (3, 6, 70),
    (4, 6, 65),
    (5, 4, 25),
    (6, 2, 80),
    (7, 2, 10),
    (8, 2, 22)
]
print(jobSequencingProblem(jobs))