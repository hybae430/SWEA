# 16진수를 2진수로
decode = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
          '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
          'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

# 1 0 1 비율
ratio = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
         '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

# 유효한 암호코드인지 판별
def check(nums):
    # 같은 암호 더하지 않도록 visited 확인
    if nums in visited:
        return 0
    # 거꾸로 저장되어 있음
    nums = nums[::-1]
    if ((nums[0] + nums[2] + nums[4] + nums[6]) * 3 + nums[1] + nums[3] + nums[5] + nums[7]) % 10:
        return 0
    else:
        return sum(nums)

# 비율 조정
def divide(x, y, z):
    minV = min(x, y, z)
    x //= minV
    y //= minV
    z //= minV
    return str(z) + str(y) + str(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    origin = [list(input()) for _ in range(N)]
    binarr = [''] * N
    for y in range(N):
        for x in range(M):
            binarr[y] += decode[origin[y][x]]
    res = []
    visited = []
    ans = 0
    for i in range(N):
        if '1' not in binarr[i]:
            continue
        x = y = z = 0
        # 뒤에서부터 세기 (모든 암호의 끝은 1임)
        for j in range(M * 4 - 1, -1, -1):
            # 첫 1
            if y == z == 0 and binarr[i][j] == '1':
                x += 1
            elif x > 0 and z == 0 and binarr[i][j] == '0':
                y += 1
            elif x > 0 and y > 0 and binarr[i][j] == '1':
                z += 1

            if x and y and z and binarr[i][j] == '0':
                # 비율 조정한 값을 dictionary에서 찾아 저장
                res.append(ratio[divide(x, y, z)])
                # 초기화
                x = y = z = 0

            if len(res) == 8:
                ans += check(res)
                visited.append(res)
                # 초기화
                res = []
    print('#{} {}'.format(tc, ans))