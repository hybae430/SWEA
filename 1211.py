def dfs(y, x):
    visited[y][x] = True
    global cnt

    if y == 99:  # base case
        return cnt

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100:  # safety_check
            if not visited[ny][nx] and lad[ny][nx] == 1:
                cnt += 1
                return dfs(ny, nx)


for tc in range(1, 11):
    tcn = input()
    lad = [list(map(int, input().split())) for _ in range(100)]
    dx = [1, -1, 0]  # 위로 올라가는건 필요 X
    dy = [0, 0, 1]
    res = -1
    min_cnt = 10000
    xs = []  # 시작점들 담을 리스트
    for i in range(100):
        if lad[0][i] == 1:
            xs.append(i)
    for x in xs:
        visited = [[False] * 100 for _ in range(100)]
        gy, gx = 0, x
        cnt = 0
        dfs(gy, gx)
        if cnt < min_cnt:
            min_cnt = cnt
            res = x
    print('#{} {}'.format(tc, res))
