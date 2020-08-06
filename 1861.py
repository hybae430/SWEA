import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    rooms = list(list(map(int, input().split())) for _ in range(N))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    res = []
    q = []

    for x in range(N):
        for y in range(N):
            cnt = 1
            q.append([x, y])
            while q:
                [a, b] = q.pop(0)
                for k in range(4):
                    nX = x + dx[k]
                    nY = y + dy[k]
                if 0 <= nX < N and 0 <= nY < N:
                    if rooms[nX][nY] == rooms[a][b] + 1:
                        q.append([nX, nY])
                        cnt += 1
            res.append([rooms[x][y], cnt])

    res = sorted(res, key = lambda x : -x[1])
    print(f'#{i} {res[0][0]} {res[0][1]}')