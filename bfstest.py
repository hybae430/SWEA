def bfs(y):
    global res

    q.append(y)
    visited.append(y)

    while q:
        y = q.pop(0)
        for x in range(V + 1):
            if node[y][x] and x not in visited:
                q.append(x)
                visited.append(x)
                if len(visited) == V + 1:
                    return

visited, q = [], []
V, E = map(int, input().split())
node = [[0] * (V + 1) for _ in range(V + 1)]
for n in range(E):
    s, g = map(int, input().split())
    node[s][g], node[g][s] = 1, 1
bfs(1)
print(visited)