T = int(input())

def dfs(x, total):
    global res

    if total >= res:
        return

    if x >= N:
        if total >= B:
            res = total
        return

    visited[x] = True
    dfs(x + 1, total + hgt[x])
    visited[x] = False
    dfs(x + 1, total)

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    hgt = list(map(int, input().split()))
    visited = [False] * N
    res = 200000
    dfs(0, 0)
    print('#{} {}'.format(tc, res - B))