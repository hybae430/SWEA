T = int(input())

def check(number):
    temp_str = str(number)
    for k in range(len(temp_str) - 1):
        if temp_str[k] > temp_str[k + 1]:
            return False
    return True

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = -1
    for i in range(N):
        for j in range(i + 1, N):
            tmp = nums[i] * nums[j]
            if result < tmp and check(tmp):
                result = tmp
    print('#{} {}'.format(tc, result))

