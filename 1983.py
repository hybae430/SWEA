import math

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = []
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(N):
        m, f, a = map(int, input().split())
        scores.append([i + 1, m * 0.35 + f * 0.45 + a * 0.2])
    scores = sorted(scores, key = lambda x : -x[1])
    for i in range(N):
        if K == scores[i][0]:
            idx = i + 1
            break
    rank = idx * 10 / N
    val = math.ceil(rank)
    print(f'#{tc} {grades[val - 1]}')
