T = int(input())

def bt(y):
    global sub, total

    if sub > total:
        return

    if y == N:
        if sub < total:
            total = sub
        return

    for x in range(N):
        if not col_check[x]:
            col_check[x] = True
            sub += mat[y][x]
            bt(y + 1)
            col_check[x] = False
            sub -= mat[y][x]

for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    col_check = [False] * N
    sub, total = 0, 100
    bt(0)

    print('#{} {}'.format(tc, total))
