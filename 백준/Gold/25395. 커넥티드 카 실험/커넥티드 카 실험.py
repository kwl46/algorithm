from collections import deque
import sys
input = sys.stdin.readline

N, S = map(int, input().split())

n_lst = [0]+list(map(int, input().split()))
h_lst = [0]+list(map(int, input().split()))

dq = deque()

dq.append(S)

ans = set()
check = [False] * (N+1)
check[S] = True

while dq:
    index = dq.popleft()

    ans.add(index)
    pos, h = n_lst[index], h_lst[index]

    for i in range(index+1, N+1):
        if (n_lst[i]-pos) > h:
            break

        if check[i]:
            continue
        check[i] = True
        dq.append(i)

    for i in range(index-1, 0, -1):
        if (pos-n_lst[i]) > h:
            break

        if check[i]:
            continue
        check[i] = True
        dq.append(i)

print(*sorted(ans))