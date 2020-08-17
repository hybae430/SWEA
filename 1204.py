from collections import Counter
T = int(input())
for tc in range(1, T + 1):
    i = input()
    score = list(map(int, input().split()))
    com = Counter(score).most_common(1)[0][0]
    print(f'#{i} {com}')