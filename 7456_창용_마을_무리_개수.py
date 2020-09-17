import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())

def dfs(y):
    for i in range(1, len(rl)):
        if rl[y][i] == 1 and i not in visited:
            visited.append(i)
            dfs(i)

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    rl = [[0] * (N + 1) for _ in range(N + 1)]
    visited = []
    cnt = 0
    for i in range(M):
        r = input()
        if len(r) > 1:
            a, b = map(int, r.split())
            rl[a][b] = rl[b][a] = 1
        else:
            rl[int(r)][int(r)] = 1
    for y in range(1, len(rl)):
        if len(visited) == N:
            break
        if y not in visited:
            cnt += 1
        dfs(y)
    print('#{} {}'.format(tc, cnt))
