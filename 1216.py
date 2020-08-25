N = 100                     # 행과 열 값

def pal_check(line):        # 회문 판단 함수 (수업시간에 한 것!)
    for idx in range(len(line) // 2):
        if line[idx] != line[-idx - 1]:
            return False
    return True

for tc in range(1, 11):     # 케이스 총 10개
    x = input()             # 날리는 값 (안씀)
    arr = [list(input()) for _ in range(N)]     # 이중배열 받는 line
    maxM = 1                                    # 가장 긴 회문의 길이를 저장하는 값 (초기값은 1: 'A'하나여도 길이는 1이기 때문)
    M = 2                                       # 1인 경우는 무조건 있으니까 조사하는 첫 값을 2로 설정
    while M <= 100:                             # 조사하는 회문의 길이가 100이 넘지 않을 경우 (행, 열 값이 100이므로)
        for i in range(N):                      # 인덱싱 (중요!!)
            for j in range(N - M + 1):          # 10짜리 열에서 7개짜리 회문 조사하려면 0, 1, 2 idx만 조사 가능
                sample = arr[i][j:j + M]        # 가로
                sample2 = [a[i] for a in arr[j:j + M]]          # 세로
                if pal_check(sample) or pal_check(sample2):     # 가로 세로 중 M길이의 회문이 있을 경우
                    maxM = M                                    # 최대값 교체
                    break                                       # 찾으면 더 돌릴필요 없으니 break
            if maxM == M:                                       # 이중포문이라 최대값 확인후 다시 break
                break
        M += 1                                                  # M을 하나 더 늘려서 100까지 돌리는 식 (비 효 율 ㅎ 100에서 줄이는게 더 낫네용)
    print('#{} {}'.format(tc, maxM))
