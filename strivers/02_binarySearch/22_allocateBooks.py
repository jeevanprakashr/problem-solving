# array of n books where arr[i] - pages in i'th book
# m students
# allocate books to to m students such that
# 1. atleast one book to each student
# 2. each book mapped to only one student
# 3. student get books only in contiguous order
# allocate books such that the maximum no. of pages among the students is the minimum
'''
Eg: [25, 46, 28, 49, 24], m = 4
=> [25 | 46 | 28 | 49, 24]  max = 49 + 24 = 73
=> [25 | 46 | 28, 49 | 24]  max = 77
=> [25 | 46, 28 | 49 | 24]  max = 74
=> [25, 46 | 28 | 49 | 24]  max = 71
Only these 4 combinations possible and minumum of these is 71, hence 71 is the answer
'''
def allocateBooks(books, m):
    '''
    Range:
    Low: - max(arr)
        - Have to make sure all the books needs to be alloted
        - If a book needs to be allotted, it should be less than the so called set maximum threshold (need to find maximum among student)
        - So the max of the given books will be set to low, since the max book should be alotted to a student
    High: - sum(arr)
        - if no. of students is 1, then all the books should be alotted to that student
        - so the high will the sum of the books
    => 49 - 172
    => 49 - 5 students
    => 172 - 1 student
    => 49, 50, 51, ........., 170, 171, 172
    => 5, ...., 4, ...., 3, ...., 2, ...., 1
    Need 4 students
    Sample:
    mid - 110  =>  2 students  =>  need 4, so anything right to 110 can't be our answer, move left
    mid - 78   =>  3 students  =>  need 4, so anything right to 78 can't be our answer, move left
    mid - 63   =>  5 students  =>  need 4, so anything left to 63 can't be our answer, move right
    mid - 69   =>  5 students  =>  need 4, so anything left to 69 can't be our answer, move right
    mid - 73   =>  4 students  =>  reached needed, but we need minumum, so move left
    mid - 71   =>  4 students  =>  possible and lesser than 73
    '''
    def numOfStudents(maxPages):
        students = 1
        totalPages = 0
        for i in range(n):
            if totalPages + books[i] <= maxPages:
                totalPages += books[i]
            else:
                students += 1
                totalPages = books[i]
        return students
    
    n = len(books)
    if m > n:
        return -1
    low = max(books)
    high = sum(books)
    while low <= high:
        mid = low + ((high - low) // 2)
        students = numOfStudents(mid)
        if students > m:
            low = mid + 1
        else:
            high = mid - 1
    return low

books = [25, 46, 28, 49, 24]
m = 4
print(allocateBooks(books, m))
