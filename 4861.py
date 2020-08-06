T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for j in range(len(arr) - M + 1):
        for k in range(j, j + M):
            