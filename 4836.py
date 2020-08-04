T = int(input())

for i in range(1, T + 1):
    pal = [[0] * 10 for i in range(10)]
    N = int(input())
    for j in range(N):
        x1, y1, x2, y2, col = map(int, input().split())
