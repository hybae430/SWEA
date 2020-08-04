T = int(input())

for i in range(1, T + 1):
    N = int(input())
    sq = list(list(map(int, input().split())) for row in range(N))
    infos = []

    for x in range(N):
        for y in range(N):
            if sq[x][y]:
                info = []
                xstart = x
                ystart = y
                while sq[xstart][y]:
                    xstart += 1
                while sq[x][ystart]:
                    ystart += 1
                info.append(xstart - x)
                info.append(ystart - y)
                info.append((xstart - x) * (ystart - y))

                for m in range(xstart - x):
                    for n in range(ystart, y):
                        sq[m][n] = 0

                infos.append(info)

    print(infos)