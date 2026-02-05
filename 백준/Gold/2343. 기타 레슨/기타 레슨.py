import sys

input = sys.stdin.readline

N, M = map(int, input().split())

n_lst = list(map(int ,input().split()))

left = max(n_lst)
right = sum(n_lst)

ans = 0

while left <= right:
    mid = (left + right) // 2

    cnt = 1
    blue = mid

    for i in range(N):
        if blue < n_lst[i]:
            cnt += 1
            blue = mid
        blue -= n_lst[i]
    
    if cnt <= M:
        ans = mid
        right = mid -1
    else:
        left = mid + 1

print(ans)