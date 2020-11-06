from heapq import heappush, heappop
INF = 1e9

def dijkstra():
    heap = []
    dist = [INF] * (N + 1)
    visited = [False] * (N + 1)
    heappush(heap, (0, 0))
    dist[0] = 0
    while heap:
        weight, node = heappop(heap)
        if not visited[node]:
            visited[node] = True
            dist[node] = weight
            for i in range(N + 1):
                if not visited[i] and (dist[i] > dist[node] + adj[node][i]):
                    heappush(heap, (dist[node] + adj[node][i], i))
    return dist[N]

# 최소 이동 거리
T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(E):
        start, end, weight = map(int, input().split())
        adj[start][end] = weight
    print('#{} {}'.format(tc, dijkstra()))
