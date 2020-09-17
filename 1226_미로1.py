N = 100
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    global res

    q.append((y, x))
    visited.append((y, x))

    while q:
        y, x = q.pop(0)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited and maze[ny][nx] != '1':
                q.append((ny, nx))
                visited.append((ny, nx))
                if maze[ny][nx] == '3':
                    res = 1
                    return

for tc in range(1, 11):
    tn = int(input())
    maze = [list(input()) for _ in range(N)]
    q, visited = [], []
    res = 0
    for y in range(N):
        for x in range(N):
            if maze[y][x] == '2':
                sy, sx = y, x
    bfs(sy, sx)
    print('#{} {}'.format(tc, res))
