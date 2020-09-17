T = int(input())

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
                dist[ny][nx] = dist[y][x] + 1
                if maze[ny][nx] == '3':
                    res = dist[ny][nx] - 1
                    return

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited, q = [], []
    dist = [[0] * N for _ in range(N)]
    res = 0
    for y in range(N):
        for x in range(N):
            if maze[y][x] == '2':
                bfs(y, x)
    print('#{} {}'.format(tc, res))
