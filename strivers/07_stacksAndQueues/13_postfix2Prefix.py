# Given an expression with operands and operators in postfix, convert it to prefix

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

def postfix2Prefix(exp):
    '''
    Eg: AB-DE+F*/
    Follow similar way as we did for postfix2Infix, but this time, instead of '(top2 op top1)',
    we do 'op top2 top1' without brackets and push it back to stack.
    char    stack
    A       A
    B       B
    -       -AB
    D       -AB, D
    E       -AB, D, E
    +       -AB, +DE
    F       -AB, +DE, F
    *       -AB, *+DEF
    /       /-AB*+DEF
    '''
    st = Stack()
    i = 0
    n = len(exp)
    while i < n:
        if (exp[i] >= 'A' and exp[i] <= 'Z') or (exp[i] >= 'a' and exp[i] <= 'z') or (exp[i] >= '0' and exp[i] <= '9'):
            st.push(exp[i])
        else:
            t1 = st.pop()
            t2 = st.pop()
            newExp = exp[i] + t2 + t1
            st.push(newExp)
        i += 1
    return st.pop()

exp = "AB-DE+F*/"
print(postfix2Prefix(exp))