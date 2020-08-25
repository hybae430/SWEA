def dfs(key):
    visited[key] = True
    for i in graph[key]:
        if not visited[i]:
            dfs(i)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {}
    visited = [False for _ in range(V + 1)]
    for i in range(E):
        fr, to = map(int, input().split())
        if fr in graph:
            graph[fr].append(to)
        else:
            graph[fr] = [to]
    S, G = map(int, input().split())
    dfs(S)
    res = 1
    if not visited[G]:
        res = 0
    print("#{} {}".format(tc, res))
