import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku2 = list(map(list, zip(*sudoku)))
    res = 1
    for i in range(9):
        check = set()       # 가로 check
        check2 = set()      # 세로 check
        for j in range(9):
            check.add(sudoku[i][j])
            check2.add(sudoku2[i][j])
        if len(check) != 9 or len(check2) != 9:
            res = 0
            break
    if res:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                check3 = set()   # 블럭 check
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        check3.add(sudoku[x][y])
                if len(check3) != 9:
                    res = 0
                    break
            if res == 0:
                break
    print('#{} {}'.format(tc, res))