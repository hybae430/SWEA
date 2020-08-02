sp = 0
line= [0] * 5
for i in range(5):
    for j in range(len(line)):
        if sp == j:
            line[j] = '#'
        else:
            line[j] = '+'
    sp += 1
    print(''.join(line))