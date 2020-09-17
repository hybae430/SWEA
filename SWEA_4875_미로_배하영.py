T = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    global found

    visited[y][x] = True

    if maze[y][x] == '3':
        found = 1
        return

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and maze[ny][nx] != '1':
            dfs(ny, nx)

for tc in range(1, T + 1):

    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    found = 0

    for y in range(N):
        for x in range(N):
            if maze[y][x] == '2':
                ty, tx = y, x

    dfs(ty, tx)

    print('#{} {}'.format(tc, found))
