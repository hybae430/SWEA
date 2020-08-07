T = int(input())

for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    av = (sum(nums) - max(nums) - min(nums)) / 8
    print(f'#{tc} {round(av)}')

for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    av = sum(sorted(nums)[1:9]) / 8
    print(f'#{tc} {round(av)}')