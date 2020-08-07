T = int(input())

for tc in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    m, ml = divmod(m1 + m2, 60)
    h = (h1 + h2) % 12 + m
    print(f'#{tc} {h} {ml}')