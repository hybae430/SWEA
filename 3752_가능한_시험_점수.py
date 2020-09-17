import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    visited = [1] + [0] * sum(nums)
    score = [0]
    for num in nums:
        for i in range(len(score)):
            if not visited[num + score[i]]:
                visited[num + score[i]] = 1
                score.append(num + score[i])
    print('#{} {}'.format(tc, len(score)))