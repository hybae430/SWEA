def dfs(y, x):
    visited[y][x] = True
    global res

    if y == 0:          # base case
        res = x
        return

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100:     # safety_check // is_safe
            if not visited[ny][nx] and lad[ny][nx] == 1:
                return dfs(ny, nx)

for tc in range(1, 11):
    tcn = input()
    lad = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]
    dx = [1, -1, 0]  # 아래로 올라가는건 필요 X
    dy = [0, 0, -1]
    res = -1 # false
    y, x = 99, lad[99].index(2)
    dfs(y, x)
    print('#{} {}'.format(tc, res))