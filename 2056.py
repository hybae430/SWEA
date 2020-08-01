T = int(input())

for i in range(1, T + 1):
    cal = input()
    y = cal[:4]
    m = cal[4:6]
    d = cal[6:]

    if int(m) > 12 or int(m) == 0 or int(d) > 31 or int(d) == 0:
        show = -1
    elif int(m) in [4, 6, 9, 11] and int(d) > 30:
        show = -1
    elif int(m) == 2 and int(d) > 28:
        show = -1
    else:
        show = f'{y}/{m}/{d}'
    
    print(f'#{i}', show)