import sys
input = sys.stdin.readline

N, M = map(int ,input().split())

n_lst = []

for i in range(N):
    n_lst.append(int(input()))

n_lst.sort()

left = 0
right = 0
min_diff = float("inf")

while left <= right:
    n1 = n_lst[left]
    n2 = n_lst[right]

    if M > (n2-n1):
        if right == N-1:
            break
        right += 1
    elif M == (n2-n1):
        min_diff = M
        break
    else:
        min_diff = min(min_diff, (n2-n1))
        left += 1

print(min_diff)