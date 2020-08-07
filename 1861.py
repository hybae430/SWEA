T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    rooms = list(list(map(int, input().split())) for _ in range(N))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    res = []

    for x in range(N):
        for y in range(N):
            q = []
            cnt = 1
            q.append([x, y])
            while q:
                [a, b] = q.pop()
                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if rooms[a][b] + 1 == rooms[nx][ny]:
                            q.append([nx, ny])
                            cnt += 1
                            break
            res.append([rooms[x][y], cnt])
    res = sorted(res, key = lambda x : (-x[1], x[0]))
    print(f'#{tc} {res[0][0]} {res[0][1]}')