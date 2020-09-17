def dfs(y, x):
    global cnt
    visited[y][x] = True
    arr[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if not visited[ny][nx] and arr[ny][nx] == '1':
                cnt += 1
                dfs(ny, nx)

N = int(input())
arr = [list(input()) for _ in range(N)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
g_cnt = 0
g_num = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            g_cnt += 1
            cnt = 1
            visited = [[False] * N for _ in range(N)]
            dfs(i, j)
            g_num.append(cnt)
g_num.sort()
print(g_cnt)
for num in g_num:
    print(num)