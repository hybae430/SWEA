from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')
INF = 1e9

# 최소 비용 (bfs - 시간 초과)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
# def bfs(y, x):
#     q = [(y, x)]
#     while q:
#         y, x = q.pop(0)
#         visited.append((y, x))
#         for i in range(4):
#             ny, nx = y + dy[i], x + dx[i]
#             if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited:
#                 q.append((ny, nx))
#                 tmp = dist[y][x] + 1
#                 if graph[ny][nx] > graph[y][x]:
#                     tmp += graph[ny][nx] - graph[y][x]
#                 if not dist[ny][nx]:
#                     dist[ny][nx] = tmp
#                 else:
#                     dist[ny][nx] = min(dist[ny][nx], tmp)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     graph = [list(map(int, input().split())) for _ in range(N)]
#     dist = [[0] * N for _ in range(N)]
#     visited = []
#     bfs(0, 0)
#     print('#{} {}'.format(tc, dist[N - 1][N - 1]))

# 다익스트라
def dijkstra():
    heap = []
    dist[0][0] = 0
    # 가중치, 행, 열
    heappush(heap, (dist[0][0], 0, 0))
    while heap:
        weight, y, x = heappop(heap)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                add_cost = graph[ny][nx] - graph[y][x]
                if add_cost < 0:
                    add_cost = 0
                new = weight + 1 + add_cost
                if dist[ny][nx] > new:
                    dist[ny][nx] = new
                    heappush(heap, (dist[ny][nx], ny, nx))
    return dist[N - 1][N - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF]*N for _ in range(N)]
    print('#{} {}'.format(tc, dijkstra()))

