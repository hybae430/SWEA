import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())

def dfs(y):
    for c in graph[y]:
        if c != y:
            if c in visited:
                if len(visited) == 3:
                    if sorted(visited) not in tri:
                        tri.append(sorted(visited))
                        return
                else:
                    return
            else:
                visited.append(c)
                dfs(c)

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    tri = []
    for m in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    for n in range(N):
        if graph[n]:
            for i in range(len(graph[n])):
                visited = []
                visited.append(graph[n][i])
                dfs(graph[n][i])
    print('#{} {}'.format(tc, len(tri)))
