T = int(input())

for i in range(1, T + 1):
    x, y = map(int, input().split())
    if x > y:
        symbol = '>'
    elif x < y:
        symbol = '<'
    else:
        symbol = '='
    print(f'#{i} {symbol}')