from collections import deque
import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())

temp_lst = list(map(int, input().split()))

money_lst = []

for i in range(N):
    money_lst.append((temp_lst[i], i))

money_lst.sort()

map_lst = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    map_lst[a].append(b)
    map_lst[b].append(a)

check = [False] * (N+1)
ans = 0
dq = deque()

for i in range(N):
    m, index = money_lst[i]
    if check[index+1]:
        continue
    check[index+1] = True
    ans += m

    dq.append(index+1)

    while dq:
        pos = dq.popleft()

        for d in map_lst[pos]:
            if check[d]:
                continue
            check[d] = True
            dq.append(d)

if ans > k:
    print("Oh no")
else:
    print(ans)