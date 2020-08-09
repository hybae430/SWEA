T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    print(f'#{tc}', end = " ")
    for num in sorted(nums):
        print(num, end = " ")
    print()