T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    if N % 2:
        total = 1 + N // 2
    else:
        total = -1 * N // 2

    print(f'#{tc} {total}')