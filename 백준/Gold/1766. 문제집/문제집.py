import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

N, M = map(int, input().split())

ans_lst = []
map_lst = [[] for _ in range(N + 1)]
inDegree = [0 for _ in range(N + 1)] # 진입 차수
hq = []

for i in range(M):
    a, b = map(int, input().split())
    map_lst[a].append(b)
    inDegree[b] += 1

for i in range(1, N + 1):
    if inDegree[i] == 0:
        push(hq, i)

while hq:
    pos = heapq.heappop(hq)
    ans_lst.append(pos)

    for i in map_lst[pos]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(hq, i)

print(*ans_lst)