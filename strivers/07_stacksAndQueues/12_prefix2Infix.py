# Given an expression with operands and operators in prefix, convert it to infix

from Stack import Stack

'''
operators priorities:
top - larger, low - smaller
3 -> ^ (power)
2 -> *, /
1 -> +, -
Eg:
infix:
    (p + q) * (m - n)
prefix:
    * + p q - m n
postfix:
    p q + m n - *
'''

def prefix2Infix(exp):
    '''
    Eg: *+PQ-MN
    Steps are same as postfix to infix with few changes
    Iterate from last character to first character instead.
    push operands to stack and when operand is encounted, pop top 2 elements and arrange like
    'top1 op top2' instead of 'top2 op top1' in postfix2Infix
    and push it back
    char    stack
    N       N
    M       N, M
    -       (M-N)
    Q       (M-N), Q
    P       (M-N), Q, P
    +       (M-N), (P+Q)
    *       ((P+Q)*(M-N))
    '''
    st = Stack()
    i = len(exp) - 1
    while i >= 0:
        if (exp[i] >= 'A' and exp[i] <= 'Z') or (exp[i] >= 'a' and exp[i] <= 'z') or (exp[i] >= '0' and exp[i] <= '9'):
            st.push(exp[i])
        else:
            t1 = st.pop()
            t2 = st.pop()
            newExp = '(' + t1 + exp[i] + t2 + ')'
            st.push(newExp)
        i -= 1
    return st.pop()

exp = "*+PQ-MN"
print(prefix2Infix(exp))