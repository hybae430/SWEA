# 보급로
from heapq import heappush, heappop
INF = 1e9
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dijkstra():
    heap = []
    dist[0][0] = 0
    heappush(heap, (dist[0][0], 0, 0))
    while heap:
        cost, y, x = heappop(heap)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not 0 <= ny < N or not 0 <= nx < N:
                continue
            if dist[ny][nx] > dist[y][x] + road[ny][nx]:
                dist[ny][nx] = dist[y][x] + road[ny][nx]
                heappush(heap, (dist[ny][nx], ny, nx))
    return dist[N - 1][N - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dist = [[INF] * N for _ in range(N)]
    road = [list(map(int, input())) for _ in range(N)]
    print('#{} {}'.format(tc, dijkstra()))