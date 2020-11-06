T = int(input())
def form(a):
    return int(a) / 100

def bt(y, mul):
    global ans

    if mul <= ans:
        return

    if y == N:
        ans = max(ans, mul)
        return

    for i in range(N):
        if not col_check[i]:
            col_check[i] = True
            bt(y + 1, mul * pcts[y][i])
            col_check[i] = False

for tc in range(1, T + 1):
    N = int(input())
    pcts = [list(map(form, input().split())) for i in range(N)]
    col_check = [False] * N
    ans = 0
    bt(0, 100)
    print('#{} {:.6f}'.format(tc, ans))
