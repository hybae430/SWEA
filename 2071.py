T = int(input())

for i in range(1, T + 1):
    numlist = map(int, input().split())
    avg = round(sum(numlist) / 10)
    print(f'#{i} {avg}')