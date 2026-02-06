import heapq
from collections import deque
import sys

input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

N = int(input())
M= int(input())

map_lst = [[] for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int ,input().split())
    map_lst[a].append((b,c))

S, D = map(int ,input().split())

hq = []

push(hq,(0,S,1,-1))

parent = [[] for _ in range(N+1)]

check = [False] * (N+1)
while hq:
    ele = pop(hq)
    cost = ele[0]
    pos = ele[1]
    lev = ele[2]
    bef = ele[3]

    if check[pos]:
        continue
    check[pos] = True
    parent[pos].append(bef)

    if pos == D:
        print(cost)
        print(lev)
        break
    for d, c in map_lst[pos]:
        if check[d]:
            continue
        
        push(hq,(cost+c, d, lev+1,pos))
    
dq = deque()
dq.append(D)
ans_lst = []

while dq:
    pos = dq.popleft()
    ans_lst.append(pos)
    for d in parent[pos]:
        if d == -1:
            break
        dq.append(d)
        break

for i in range(len(ans_lst)-1, -1, -1):
    print(ans_lst[i], end=" ")
