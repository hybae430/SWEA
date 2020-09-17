import sys

sys.stdin = open('sample_input(1).txt', 'r')

T = int(input())
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    mid = N // 2
    board[mid][mid] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1
    board[mid - 1][mid - 1] = 2
    for i in range(M):
        x, y, c = map(int, input().split())
        x, y = x - 1, y - 1
        reverse = []
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            while True:
                if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                    reverse = []
                    break
                elif board[nx][ny] == 0:
                    reverse = []
                    break
                elif board[nx][ny] == c:
                    break
                else:
                    reverse.append((nx, ny))
                nx, ny = nx + dx[j], ny + dy[j]
            for m, n in reverse:
                board[m][n] = c
        board[x][y] = c
    cnt1, cnt2 = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] == 2:
                cnt2 += 1
    print('#{} {} {}'.format(tc, cnt1, cnt2))
