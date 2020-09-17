import sys
sys.stdin = open('sample_input(1).txt', 'r')


T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())

    # 초기설정
    board = [[0] * N for _ in range(N)]
    mid = N // 2
    board[mid][mid] = 2
    board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1

    # 델타설정
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, -1, -1, 0, 1]

    # 입력값 받기
    for i in range(M):
        x, y, z = map(int, input().split())
        x, y = x - 1, y - 1
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            reverse = []
            while True:
                if 0 > nx or 0 > ny or N - 1 < nx or N - 1 < ny:    # 모서리 나가는 애들
                    reverse = []
                    break
                elif board[nx][ny] == 0:
                    reverse = []
                    break
                elif board[nx][ny] == z:
                    break
                else:
                    reverse.append((nx, ny))
                nx += dx[j]
                ny += dy[j]
            for m, n in reverse:
                board[m][n] = z
        board[x][y] = z

    # 흑백 수 세기
    cnt1, cnt2 = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] == 2:
                cnt2 += 1

    print('#{} {} {}'.format(tc, cnt1, cnt2))