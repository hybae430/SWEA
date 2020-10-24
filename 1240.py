T = int(input())
# 코드 dictionary
code = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5', '0101111': '6',
        '0111011': '7', '0110111': '8', '0001011': '9'}

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 없으면 0 출력이므로 ans는 0으로 초기화
    # 뒤에서부터 1의 index는 없는 값인 -1로 초기화 (암호 1개 무조건 존재)
    ans, idx = 0, -1
    # 암호값이 유효한지 판단하는 boolean 변수
    flag = True
    line = ''

    for n in range(N):
        s = input()
        # 찾았을 경우에도 input은 다 받아줘야 다음 tc 진행 가능함
        # 그래서 continue로 idx 찾았을 경우 넘겨줌
        if idx > -1:
            continue
        # str로 받았기 때문에 '1'이 들어있는지 판단 후 맨 뒤 숫자가 1이라는 점을 이용해 idx 구하기
        # 따로 '1'이 들어있던 string을 line으로 저장
        if '1' in s:
            idx = list(reversed(s)).index('1')
            line = s

    # indexing해서 암호 string 만들기
    line = line[M - idx - 56:M - idx]
    # 암호값 저장할 string
    tmp = ''
    for i in range(0, 56, 7):
        # dictionary에 없는 값이 들어올 수 있으므로 get을 이용해 에러 안뜨도록 함
        # 없는 경우 'none'을 대신 더해줌
        tmp += code.get(line[i:i + 7], 'none')
        # 'none'이 tmp에 들어있을 경우 flag를 false로 바꾸고 break
        if 'none' in tmp:
            flag = False
            break

    # 암호가 유효할 경우만
    if flag:
        # 홀수, 짝수번째 자릿수 합 저장할 변수
        odd, even = 0, 0
        for i in range(len(tmp) - 1):
            if not i % 2:
                odd += int(tmp[i])
            else:
                even += int(tmp[i])
        # 판별식이 10으로 나누어떨어지지 않을 경우 잘못된 암호
        # flag를 false로 바꿔줌
        if (odd * 3 + even + int(tmp[-1])) % 10:
            flag = False
        else:
            ans = odd + even + int(tmp[-1])

    print('#{} {}'.format(tc, ans))