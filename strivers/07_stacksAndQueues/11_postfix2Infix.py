# Given an expression with operands and operators in postfix, convert it to infix

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

def postfix2Infix(exp):
    '''
    Eg: AB-DE+F*/
    => When it is an operand, push it to stack
    => When it is an operator, pop top 2 elements from stack, arrange like 'top2 op top1' and wrap them with brackets, and push back the resulting expression into the stack
    At last, there will be only one element in the stack, which is our answer
    char    stack
    A       A
    B       A, B
    -       (A-B)
    D       (A-B), D
    E       (A-B), D, E
    +       (A-B), (D+E)
    F       (A-B), (D+E), F
    *       (A-B), ((D+E)*F)
    /       ((A-B)/((D+E)*F))
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
            newExp = '(' + t2 + exp[i] + t1 + ')'
            st.push(newExp)
        i += 1
    return st.pop()

exp = "AB-DE+F*/"
print(postfix2Infix(exp))