T = int(input())

def dfs(y, total):
    global ans

    if total >= ans:
        return

    if y == N:
        if total >= B:
            ans = total
        return

    visited[y] = True
    dfs(y + 1, total + heights[y])
    visited[y] = False
    dfs(y + 1, total)

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    visited = [False] * N
    ans = 200000
    dfs(0, 0)
    print('#{} {}'.format(tc, ans - B))

