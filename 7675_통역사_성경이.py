import sys
sys.stdin = open('s_input.txt', 'r')

sep = ['.', '?', '!']
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    s = input()
    sentence = []
    tmp = 0
    print('#{}'.format(tc), end=" ")
    for idx, i in enumerate(s):
        if i in sep:
            sentence.append(s[tmp:idx + 1])
            tmp = idx + 2
    for sen in sentence:
        words = sen.split()
        cnt = 0
        for word in words:
            isname = 1
            for i in range(len(word)):
                if i == 0:
                    if not word[i].isupper():
                        isname = 0
                        break
                elif i != 0 and i != len(word) - 1:
                    if not word[i].islower():
                        isname = 0
                        break
                elif i == len(word) - 1:
                    if not (word[i].islower() or word[i] in sep):
                        isname = 0
                        break
            if isname:
                cnt += 1
        print(cnt, end=" ")
    print()