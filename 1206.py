import sys

for i in range(1, 11):
    N = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    total = 0

    for j in range(2, N - 2):
        tmp = heights[j]
        left1, left2, right1, right2 = heights[j - 2], heights[j - 1], heights[j + 1], heights[j + 2]
        if left1 <= tmp and left2 <= tmp and right1 <= tmp and right2 <= tmp:
            total += min(tmp - left1, tmp - left2, tmp - right1, tmp - right2)
    
    print(f'#{i} {total}')