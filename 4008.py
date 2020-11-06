import sys
sys.stdin = open('sample_input.txt')

def dfs(n, total):
    global minV, maxV
    if n == (N - 1):
        if total >= maxV:
            maxV = total
        if total <= minV:
            minV = total
        return

    for i in range(4):
        if signs[i]:
            signs[i] -= 1
            if i == 0:
                tmp = total + nums[n + 1]
            elif i == 1:
                tmp = total - nums[n + 1]
            elif i == 2:
                tmp = total * nums[n + 1]
            elif i == 3:
                tmp = int(total / nums[n + 1])
            dfs(n + 1, tmp)
            signs[i] += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    signs = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    minV, maxV, ans = 100000000, -100000000, 0
    dfs(0, nums[0])
    ans = maxV - minV
    print('#{} {}'.format(tc, ans))