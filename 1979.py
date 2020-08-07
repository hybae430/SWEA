import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    word = []
    row_visited = [[False] * N for _ in range(N)]
    col_visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            row_cnt, col_cnt = 0, 0
            dx, dy = j, j
            while board[i][dx] and not row_visited[i][dx]:
                row_cnt += 1
                row_visited[i][dx] = True
                if dx >= N - 1:
                    break
                else:
                    dx += 1
            while board[dy][i] and not col_visited[dy][i]:
                col_cnt += 1
                col_visited[dy][i] = True
                if dy >= N - 1:
                    break
                else:
                    dy += 1
            if col_cnt > 1:
                word.append(col_cnt)
            if row_cnt > 1:
                word.append(row_cnt)

    print(f'#{tc} {word.count(K)}')