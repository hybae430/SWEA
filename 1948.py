T = int(input())
m = [i for i in range(1, 11)]
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T + 1):
    days = 0
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2:
        days = d2 - d1
    else:
        for i in range(m1 + 1, m2):
            days += d[i - 1]
        days += d[m1 - 1] - d1 + d2
    print(f'#{tc} {days + 1}')