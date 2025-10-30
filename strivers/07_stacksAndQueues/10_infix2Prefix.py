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

def reverse(exp):
    res = ""
    n = len(exp)
    for i in range(n - 1, -1, -1):
        if exp[i] == '(':
            res += ')'
        elif exp[i] == ')':
            res += '('
        else:
            res += exp[i]
    return res


def infix2Prefix(exp):
    '''
    Steps:
    1. Reverse the exp - once reversed, change ( -> ) and ) -> (
    2. Do infix to postfix as we did in previous problem with a slight change
        In infix to postfix, when we see operand, if priority(op) <= stack.top(), then we do pop till stack.top() < priority(op)
        i.e, if op = '+' and stack.top() = '-', even though '+' = '-' in priority, we pop '-' and push '+' into stack
        but here, we strictly check for priority(op) < stack.pop() except if the op = '^'
        if '^', then we check for <=
        i.e, if op = '+' and stack.top() = '-', we simply push '+' into stack
    3. Reverse the postfix exp and return the same
    Eg:
    (A + B) * C - D + F
    ans = +-*+ABCDF
    '''
    exp = reverse(exp)
    st = Stack()
    i = 0
    n = len(exp)
    ans = ""
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
            if exp[i] == '^':
                while not st.isEmpty() and prio(exp[i]) <= prio(st.top()):
                    ans += st.pop()
            else:
                while not st.isEmpty() and prio(exp[i]) < prio(st.top()):
                    ans += st.pop()
            st.push(exp[i])
        i += 1
    while not st.isEmpty():
        ans += st.pop()
    return reverse(ans)

exp = "(A+B)*C-D+F"
print(infix2Prefix(exp))