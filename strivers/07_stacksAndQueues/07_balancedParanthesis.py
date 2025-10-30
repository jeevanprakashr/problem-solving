def balancedParanthesis(pStr):
    st = []
    for c in pStr:
        if c in "([{":
            st.append(c)
        else:
            if len(st) == 0:
                return False
            top = st.pop()
            if not ((c == ')' and top == '(') or (c == ']' and top == '[') or (c == '}' and top == '{')):
                return False
    return len(st) == 0

pStr = "()[{}(]"
print(balancedParanthesis(pStr))