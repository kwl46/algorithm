from collections import deque
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

map_lst = []

for i in range(N):
    s = input().strip()
    temp_lst = list(map(int, s))
    map_lst.append(temp_lst)

dq = deque()

check = [[[False]*(K+1) for _ in range(M)] for _ in range(N)]

dq.append((1,0,0,0))
check[0][0][0] = True
dr = [1,0,-1,0]
dc = [0,1,0,-1]
ans = float("inf")

while dq:
    cost, k, r, c = dq.popleft()

    if r == N-1 and c == M-1:
        ans = min(ans, cost)
        break

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]

        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
            continue
        if map_lst[next_r][next_c] == 1:
            if k == K:
                continue
            else:
                if check[next_r][next_c][k+1]:
                    continue
                check[next_r][next_c][k+1] = True
                dq.append((cost+1,k+1,next_r,next_c))
        else:
            if check[next_r][next_c][k]:
                continue
            check[next_r][next_c][k] = True
            dq.append((cost+1,k,next_r,next_c))
            
if ans == float("inf"):
    print(-1)
else:
    print(ans)