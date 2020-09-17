T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    chz = list(map(int, input().split()))
    q = []
    for i in range(1, N + 1):
        q.append([i, chz[i - 1]])
    idx = 1                         # 다음 피자 인덱스를 위한 수
    while len(q) != 1:
        q[0][1] //= 2
        if q[0][1] == 0:
            if N + idx - 1 < M:     # 더 넣을게 있으면
                q.pop(0)
                q.append([N + idx, chz[N + idx - 1]])
                idx += 1
            else:
                q.pop(0)            # 더 넣을게 없으면
        else:
            q.append(q.pop(0))      # 맨 뒤로 보내기
    print('#{} {}'.format(tc, q[0][0]))
