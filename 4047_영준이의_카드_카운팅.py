import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

# for tc in range(1, T + 1):
#
#     line = input()
#     cards = []
#     S, D, H, C = [], [], [], []
#     start, end = 0, 3
#     res = ''
#
#     while True:
#         cards.append(line[start:end])
#         if end >= len(line):
#             break
#         else:
#             start = end
#             end += 3
#
#     for card in cards:
#         if card[0] == 'S':
#             if card[1:3] not in S:
#                 S.append(card[1:3])
#             else:
#                 res = 'ERROR'
#         elif card[0] == 'D':
#             if card[1:3] not in D:
#                 D.append(card[1:3])
#             else:
#                 res = 'ERROR'
#         elif card[0] == 'H':
#             if card[1:3] not in H:
#                 H.append(card[1:3])
#             else:
#                 res = 'ERROR'
#         else:
#             if card[1:3] not in C:
#                 C.append(card[1:3])
#             else:
#                 res = 'ERROR'
#
#     if res != 'ERROR':
#         res = '{} {} {} {}'.format(13 - len(S), 13 - len(D), 13 - len(H), 13 - len(C))
#
#     print('#{} {}'.format(tc, res))

for tc in range(1, T + 1):
    line = input()
    cards = []
    res = {'S':13, 'D':13, 'H':13, 'C':13}
    for i in range(0, len(line), 3):
        cards.append(line[i:i+3])
    if len(set(cards)) != len(cards):
        print('#{} {}'.format(tc, 'ERROR'))
    else:
        for card in cards:
            res[card[0]] -= 1
        print('#{}'.format(tc), end=" ")
        print(*res.values())