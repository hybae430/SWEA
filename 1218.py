for tc in range(1, 11):
    n = input()
    line = input()
    st = []  # stack list
    res = 1
    for l in line:
        if l == '(' or l == '{' or l == '[' or l == '<':
            st.append(l)
        elif (l == ')' or l == '}' or l == ']' or l == '>') and len(st):
            if l == ')' and st[-1] == '(':
                st.pop()
            elif l == '}' and st[-1] == '{':
                st.pop()
            elif l == ']' and st[-1] == '[':
                st.pop()
            elif l == '>' and st[-1] == '<':
                st.pop()
            else:
                res = 0
                break
        elif (l == ')' or l == '}' or l == ']' or l == '>') and len(st) == 0:
            res = 0
            break
    if len(st):
        res = 0
    print('#{} {}'.format(tc, res))
