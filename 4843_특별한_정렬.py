T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     res = []
#     while len(nums) > 1:
#         M, m = max(nums), min(nums)
#         res.append(M)
#         nums.remove(M)
#         res.append(m)
#         nums.remove(m)
#     if nums:
#         res.append(nums[0])
#     print('#{}'.format(tc), end=" ")
#     for r in res[:10]:
#         print(r, end=" ")
#     print()

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    res = []
    for i in range(len(nums) // 2):
        res.append(nums[i])
        res.append(nums[len(nums) - i - 1])
    if len(nums) % 2:
        res.append(nums[len(nums // 2)])
    print('#{}'.format(tc), end=" ")
    for r in res[:10]:
        print(r, end=" ")
    print()