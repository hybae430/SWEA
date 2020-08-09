T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = [[] * N]
    for i in range(1, N * N):
        idx = 0
        if idx < N:
            numbers[0][idx] = idx + 1
        elif idx < 2 * N - 1:
            numbers[idx - N + 1][N - 1] = idx + 1
        elif idx < 3 * N - 2:
