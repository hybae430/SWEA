import pandas as pd
members = ['배하영', '김진영', '박수아', '김근영', '신민호',
 '이현우', '강은묵', '김지형', '구진범', '김채린', '이병훈',
  '최주아', '김문정', '전의수', '박승범', '이동훈', '정선영', '박봉현']
prob = ['최대수 구하기', '자릿수 더하기', '중간값 찾기']
O = {}
xl = pd.read_excel(r'C:\Users\viole\Desktop\SWEA0731.xlsx', header = 1)
for idx, name in enumerate(xl['닉네임']):
    if name[:3] not in O:
        O[name[:3]] = []
        O[name[:3]].append(xl['문제이름'][idx])

    else:
        if xl['문제이름'][idx] not in O[name[:3]]:
            O[name[:3]].append(xl['문제이름'][idx])

print('---벌금---')
print('덜푼사람:', end = " ")
for key in O.keys():
    if len(O[key]) < 3:
        print(key, end = " ")
tmp = set(members) - set(O.keys())
print('\n미참여자: ', tmp)