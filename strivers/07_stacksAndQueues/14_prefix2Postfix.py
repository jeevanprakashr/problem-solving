# Given an expression with operands and operators in prefix, convert it to postfix

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

def prefix2Postfix(exp):
    '''
    Eg: /-AB*+DEF
    Follow similar way as we did for prefix2Infix (iterate in reverse), but this time, instead of '(top1 op top2)',
    we do 'top1 top2 op' without brackets and push it back to stack.
    char    stack
    F       F
    E       F, E
    D       F, E, D
    +       F, DE+
    *       DE+F*
    B       DE+F*, B
    A       DE+F*, B, A
    -       DE+F*, AB-
    /       AB-DE+F*/
    '''
    st = Stack()
    i = len(exp) - 1
    while i >= 0:
        if (exp[i] >= 'A' and exp[i] <= 'Z') or (exp[i] >= 'a' and exp[i] <= 'z') or (exp[i] >= '0' and exp[i] <= '9'):
            st.push(exp[i])
        else:
            t1 = st.pop()
            t2 = st.pop()
            newExp = t1 + t2 + exp[i]
            st.push(newExp)
        i -= 1
    return st.pop()

exp = "/-AB*+DEF"
print(prefix2Postfix(exp))