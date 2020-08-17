T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 1
    numset = set()
    # 0~9가 다 들어있을 때 break
    while len(numset) < 10:
        for s in str(cnt * N):
            numset.add(s)
        cnt += 1
    print(f'#{tc} {(cnt - 1) * N}')