# Given an expression with operands and operators in infix, convert it to postfix

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

def prio(ch):
    if ch == '^':
        return 3
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '+' or ch == '-':
        return 1
    return -1

def infix2Postfix(exp):
    '''
    Using stack and some rules
    iterate through every character
    operands -> append to answer
    ( -> push to stack
    ) -> pop and append to answer until ( gets popped
    operator -> top of stack is less prio or ( or no elements in stack -> push to stack
                top of stack is high prio -> pop and append to answer until less prio or ( gets to top and then push
    Eg:
    a + b * (c ^ d - e)
    char    stack   answer
    a               a
    +       +       a
    b       +       ab
    *       +*      ab
    (       +*(     ab
    c       +*(     abc
    ^       +*(^    abc
    d       +*(^    abcd
    -       +*(     abcd^
            +*(-
    e       +*(-    abcd^e
    )       +*(     abcd^e-
            +*      
            +       abcd^e-*
                    abcd^e-*+
    '''
    st = Stack()
    i = 0
    ans = ""
    n = len(exp)
    while i < n:
        if (exp[i] >= 'A' and exp[i] <= 'Z') or (exp[i] >= 'a' and exp[i] <= 'z') or (exp[i] >= '0' and exp[i] <= '9'):
            ans += exp[i]
        elif exp[i] == '(':
            st.push(exp[i])
        elif exp[i] == ')':
            while not st.isEmpty() and st.top() != '(':
                ans += st.pop()
            st.pop()
        else:
            while not st.isEmpty() and prio(exp[i]) <= prio(st.top()):
                ans += st.pop()
            st.push(exp[i])
        i += 1
    while not st.isEmpty():
        ans += st.pop()
    return ans

exp = "a+b*(c^d-e)"
print(infix2Postfix(exp))