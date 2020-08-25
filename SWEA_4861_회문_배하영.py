T = int(input())                                    # tc개수

def pal_check(line):                                # 회문 체크 수업시간함수
    for idx in range(len(line) // 2):
        if line[idx] != line[-idx - 1]:
            return False
    return True

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    found = False                                   # 루프 깨줄 변수
    arr = [list(input()) for _ in range(N)]
    print('#{}'.format(tc), end = " ")
    for i in range(N):
        for j in range(N - M + 1):
            sample = arr[i][j:j + M]                # 가로
            sample2 = [a[i] for a in arr[j:j + M]]  # 세로
            if pal_check(sample):                   # 가로에서 회문 찾을 경우
                print(''.join(sample))              # 하나로 합쳐주기
                found = True                        # 찾았다
                break
            elif pal_check(sample2):                # 세로에서 회문 찾을 경우
                found = True                        # 찾았다
                print(''.join(sample2))
        if found:                                   # 회문 1개뿐이므로 찾았으면 루프 깨주기
            break