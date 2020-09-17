import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    global cnt

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and sq[ny][nx] == sq[y][x] + 1:
            cnt += 1
            dfs(ny, nx)
    return cnt

for tc in range(1, T + 1):
    N = int(input())
    sq = [list(map(int, input().split())) for _ in range(N)]
    res = []
    for y in range(N):
        for x in range(N):
            cnt = 1
            res.append([sq[y][x], dfs(y, x)])
    res = sorted(res, key=lambda x: (-x[1], x[0]))
    print('#{} {} {}'.format(tc, res[0][0], res[0][1]))