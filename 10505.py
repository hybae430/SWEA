T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    aver = sum(num) / N
    num = sorted(num)
    for i in range(N):
        if num[i] > aver:
            cnt = i
            break
    else:
        cnt = N
    print(f'#{tc} {cnt}')