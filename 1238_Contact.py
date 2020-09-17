def dfs(y):
    global res
    cnt = 0
    q.append(y)
    visited.append(y)
    while q:
        x = q.pop(0)
        for i in n_list[x]:
            if i not in visited:
                q.append(i)
                visited.append(i)
                dist[i] = dist[x] + 1
                if dist[i] > cnt:
                    cnt = dist[i]
    for idx, d in enumerate(dist[::-1]):
        if d == cnt:
            res = 100 - idx
            break

for tc in range(1, 11):
    E, S = map(int, input().split())
    nodes = list(map(int, input().split()))
    n_list = [[] for _ in range(101)]
    visited, q = [], []
    res = 0
    dist = [0] * 101
    for i in range(0, E, 2):
        n_list[nodes[i]].append(nodes[i + 1])
    dfs(S)
    print('#{} {}'.format(tc, res))