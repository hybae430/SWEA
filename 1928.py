# 디코더 모듈 이용
import base64
T = int(input())
for tc in range(1, T + 1):
    s = input()
    b = base64.b64decode(s)
    print(f'#{tc}', b.decode("UTF-8"))