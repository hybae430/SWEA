A, B = map(int, input().split())

if abs(A - B) == 2:
    print('B') if A > B else print('A')
elif abs(A - B) == 1:
    print('A') if A > B else print('B')