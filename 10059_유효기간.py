T = int(input())
for tc in range(1, T + 1):
    code = input()
    ans = ''
    a = int(code[:2])
    b = int(code[2:])
    if 0 <= a < 13 and 0 <= b < 13:
        ans = 'AMBIGUOUS'
    elif 0 <= a < 13:
        ans = 'MMYY'
    elif 0 <= b < 13:
        ans = 'YYMM'
    else:
        ans = 'NA'
    print('#{} {}'.format(tc, ans))