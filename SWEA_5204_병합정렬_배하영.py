import sys
sys.stdin = open('sample_input.txt')

# 병합정렬
def mergesort(arr):
    global cnt
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)

def merge(left, right):
    res = []
    lidx, ridx = 0, 0
    idx = 0

    while lidx != len(left) and ridx != len(right):
        if left[lidx] <= right[ridx]:
            res.append(left[lidx])
            lidx += 1
        else:
            res.append(right[ridx])
            ridx += 1
        idx += 1

    while lidx != len(left):
        res.append(left[lidx])
        idx += 1
        lidx += 1

    while ridx != len(right):
        res.append(right[ridx])
        idx += 1
        ridx += 1

    return res

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    nums = list(map(int, input().split()))
    ans = mergesort(nums)
    print('#{} {} {}'.format(tc, ans[N//2], cnt))