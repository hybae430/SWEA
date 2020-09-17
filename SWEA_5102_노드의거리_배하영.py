T = int(input())

def bfs(y):
    global res

    q.append(y)
    visited.append(y)

    while q:
        y = q.pop(0)
        for x in range(1, V + 1):
            if node[y][x] and x not in visited:
                q.append(x)
                visited.append(x)
                dist[x] = dist[y] + 1
                if x == G:
                    res = dist[x]
                    return

for tc in range(1, T + 1):

    V, E = map(int, input().split())
    node = [[0] * (V + 1) for _ in range(V + 1)]
    visited, q = [], []
    dist = [0] * (V + 1)
    res = 0

    # 인접행렬
    for n in range(E):
        y, x = map(int, input().split())
        node[y][x], node[x][y] = 1, 1

    S, G = map(int, input().split())
    bfs(S)
    print('#{} {}'.format(tc, res))