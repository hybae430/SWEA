T = int(input())

for i in range(1, T + 1):
    isSudoku = True
    sudoku = list(list(map(int, input().split())) for row in range(9))

    for x in range(9):
        rowset = set()
        colset = set()
        for y in range(9):
            rowset.add(sudoku[x][y])
            colset.add(sudoku[y][x])
        if len(rowset) != 9 or len(colset) != 9:
            isSudoku = False
            break

    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            box = set()
            for m in range(x, x + 3):
                for n in range(y, y + 3):
                    box.add(sudoku[m][n])
            if len(box) != 9:
                isSudoku = False
                break
        if not isSudoku:
            break

    print('#{} {}'.format(i, int(isSudoku)))