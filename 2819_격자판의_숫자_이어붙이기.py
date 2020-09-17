T = int(input())
N = 4

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(idx, y, x, num):
    num += board[y][x]
    # 7번째 숫자까지 더했을 때 배열에 삽입
    if idx == 6:
        res.append(num)
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            dfs(idx + 1, ny, nx, num)

for tc in range(1, T + 1):
    board = [input().split() for _ in range(N)]
    res = []
    for y in range(N):
        for x in range(N):
            dfs(0, y, x, "")
    # 중복 제거
    res = set(res)
    print('#{} {}'.format(tc, len(res)))