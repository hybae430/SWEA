T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    # 처음 뺄 값 (2^-1)
    idx = 0.5
    ans = ''
    while N != 0:
        # 이미 소수점이 12자리일 경우 ans값 overflow로 변경하고 break
        if len(ans) == 12:
            ans = 'overflow'
            break
        if N - idx >= 0:
            ans += '1'
            # N 재정의
            N -= idx
        else:
            ans += '0'
        # idx 재정의
        idx /= 2
    print('#{} {}'.format(tc, ans))