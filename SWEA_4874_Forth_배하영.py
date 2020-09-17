T = int(input())
fn = ['+', '-', '*', '/']

def is_num(x):
    if x not in fn:
        return True
    return False

for tc in range(1, T + 1):
    postfix = input().split()
    ans = []
    if postfix[-1] == '.':
        postfix.pop()
    else:
        ans.append('error')
    if 'error' not in ans:
        for p in postfix:
            if is_num(p):
                ans.append(p)
            else:
                if p in fn:
                    if len(ans) > 1:
                        y, x = int(ans.pop()), int(ans.pop())
                        if p == '+':
                            ans.append(x + y)
                        elif p == '-':
                            ans.append(x - y)
                        elif p == '*':
                            ans.append(x * y)
                        elif p == '/':
                            ans.append(x // y)
                    else:
                        ans.append('error')
                        break
    if len(ans) > 1:
        ans.append('error')
    print('#{} {}'.format(tc, ans[-1]))