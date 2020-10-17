T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    avg = sum(nums) / len(nums)
    cnt = 0
    for num in nums:
        if num <= avg:
            cnt += 1
    print('#{} {}'.format(tc, cnt))