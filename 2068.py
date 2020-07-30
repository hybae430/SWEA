T = int(input())

for i in range(1, T + 1):
    numlist = map(int, input().split())
    biggest = max(numlist)
    print(f'#{i} {biggest}')