import sys
sys.stdin = open('input.txt', 'r')

# T = int(input())
#
# for i in range(1, T + 1):
#     N = int(input())
#     sq = list(list(map(int, input().split())) for row in range(N))
#     dic = {}
#
#     for y in range(N):
#         cnt = 0
#         for x in range(N):
#             if sq[y][x]:
#                 cnt += 1
#             elif sq[y][x] == 0 and cnt != 0:
#                 dic[cnt] = dic.get(cnt, 0) + 1
#                 cnt = 0
#         if cnt > 0:
#             dic[cnt] = dic.get(cnt, 0) + 1
#     matrix = []
#     for c, r in dic.items():
#         matrix.append((c * r, r, c))
#     matrix.sort()
#     print(f'#{i} {len(matrix)}', end = ' ')
#     for i in range(len(matrix)):
#         print(matrix[i][1], matrix[i][2], end = ' ')
#     print()

def width(i, j):
    count = 1
    dx = j
    while True:
        dx += 1
        if dx >= N:
            break
        if numbers[i][dx] != 0:
            count += 1
        else:
            break
    return count

def height(i, j):
    count = 1
    dy = i
    while True:
        dy += 1
        if dy >= N:
            break
        if numbers[dy][j] != 0:
            count += 1
        else:
            break
    return count

def change(a, b, c, d):
    for i in range(a, c):
        for j in range(b, d):
            numbers[i][j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    answer_list = []
    for i in range(N):
        for j in range(N):
            if numbers[i][j]:
                w = width(i, j)
                h = height(i, j)
                change(i, j, i + h, j + w)
                answer_list.append([h, w, h * w])
    answer_list = sorted(answer_list, key=lambda x: (x[2], x[0]))
    print('#{} {}'.format(t, len(answer_list)), end=' ')
    for r, c, _ in answer_list:
        print('{} {}'.format(r, c), end=' ')
    print()