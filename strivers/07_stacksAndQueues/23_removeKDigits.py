# given a number as a string and k, remove any k no. of digits such that the resulting number is the smallest
# sample: num = 1432219     k = 3
# removing 4, 3, and last 1  ->  1229
# removing 4, 3, 2  ->  1219
# like this, we can generate many combination and 1219 is the smallest among them all

from Stack import Stack

def removeKDigits(num, k):
    '''
    Our solution is greedy approach. Try to keep the beginning of the number smaller and remove any larger number encountered.
    Eg: num = 1432219     k = 3
    char = 1:
        so far no number in our result. Hence
        res = 1
    char = 4:
        we have our res starting with 1. It doesn't make sense to replace is with 4 as it will only make is larger
        so add it to our res
        res = 14
    char = 3:
        now it makes sense to replace 4 with smaller number 3 to make our res smaller
        res = 13
        k will become 2 and we used up one removal
    char = 2:
        2 < 3, so 2 replaces 3
        res = 12
        k = 1
    char = 2:
        replacing 2 with 2 itself doesn't make sense. so add it to res
        res = 122
        k = 1
    char = 1:
        now 1 < 2
        replacing 2 with 1
        res = 121
        k = 0
    char = 9:
        since we have exhausted our k, just add the remaining numbers to the res
        res = 1219
    
    This application is similar to using stack and finally returning the reversed stack elements

    Edge cases:
    case 1:
        k <= n
        so if k == n, simply return 0
    
    case 2:
        what if resulting number has trailing 0s like "00100".
        This is not a valid number hence remove the starting 0s
    
    case 3:
        k remains not exhausted
        eg: num = 123456 k = 3
        here all elements will be pushed to stack and k remains as 3
        in this case remove the top k elements from stack and return the result
    '''
    st = Stack()
    n = len(num)
    for i in range(n):
        while not st.isEmpty() and k > 0 and st.top() > num[i]:
            st.pop()
            k -= 1
        st.push(num[i])
    while k > 0:
        st.pop()
        k -= 1
    if st.isEmpty():
        return "0"
    res = ""
    while not st.isEmpty():
        res += st.pop()
    for c in res:
        st.push(c)
    while not st.isEmpty() and st.top() == "0":
        st.pop()
    if st.isEmpty():
        return "0"
    res = ""
    while not st.isEmpty():
        res += st.pop()
    return res

num = "1432219"
num = "10032"
k = 2
print(removeKDigits(num, k))
