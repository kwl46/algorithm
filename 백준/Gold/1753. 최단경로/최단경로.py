import heapq
import sys

input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

V, E = map(int, input().split())
K = int(input())

map_lst = [[] for _ in range(V+1)]

dist_lst = [float("inf")] * (V+1)

for i in range(E):
    u, v, w = map(int, input().split())
    map_lst[u].append((v,w))

hq = []

push(hq, (0, K))

while hq:
    cost, pos = pop(hq)

    if dist_lst[pos] <= cost:
        continue
    dist_lst[pos] = cost

    for d, c in map_lst[pos]:
        if dist_lst[d] <= (cost+c):
            continue
        push(hq, (cost+c, d))


for i in range(1, len(dist_lst)):
    if dist_lst[i] == float("inf"):
        print("INF")
    else:
        print(dist_lst[i])