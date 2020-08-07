for i in range(10):
    tc = 4
    tc = int(input())
    maze = list(list(input()) for _ in range(16))
    visited = [[False] * 16 for _ in range(16)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q, end = [], []
    ismaze = 0

    for x in range(16):
        for y in range(16):
            if maze[x][y] == '2':
                q.append([x, y])

    while q and not ismaze:
        [a, b] = q.pop()
        # print(a, b)
        if not visited[a][b]:
            visited[a][b] = True
        else:
            continue
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != '1' and not visited[nx][ny]:
                if maze[nx][ny] == '3':
                    ismaze = 1
                    break
                q.append([nx, ny])

    print(f'#{tc} {ismaze}')