from collections import deque
import sys
sys.stdin = open('input.txt')
# 탈주범 검거
direct = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((0, 1), (-1, 0)),
    5: ((0, 1), (1, 0)),
    6: ((0, -1), (1, 0)),
    7: ((0, -1), (-1, 0))
}

def bfs():
    global cnt
    q = deque([(R, C)])
    dist = [[0] * M for _ in range(N)]
    dist[R][C] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in direct[tunnel[y][x]]:
            ny, nx = y + dy, x + dx
            if not 0 <= ny < N or not 0 <= nx < M:
                continue
            if (-dy, -dx) in direct[tunnel[ny][nx]]:
                if not dist[ny][nx] and tunnel[ny][nx]:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
                    if dist[ny][nx] <= L:
                        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1
    print('#{} {}'.format(tc, bfs()))