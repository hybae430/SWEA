T = int(input())

for i in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    diff = max(numbers) - min(numbers)
    print(f'#{i} {diff}')