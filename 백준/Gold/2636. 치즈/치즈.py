import heapq, sys

input = sys.stdin.readline

push = heapq.heappush
pop = heapq.heappop

N, M = map(int, input().split())

map_lst = []

for i in range(N):
    map_lst.append(list(map(int, input().split())))

dr = [1,0,-1,0]
dc = [0,1,0,-1]

hq =[]

T_lst = [0] * 101

check = [[False] * (M) for _ in range(N)]
push(hq, (0,0,0))
max_time = 0

while hq:
    time, r, c = pop(hq)
    if map_lst[r][c] == 1:
        T_lst[time] += 1

    max_time = max(max_time, time)

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
            continue
        if check[next_r][next_c]:
            continue
        check[next_r][next_c] = True
        if map_lst[next_r][next_c] == 1:
            push(hq,(time+1, next_r, next_c))
        else:
            push(hq,(time,next_r,next_c))

print(max_time)
print(T_lst[max_time])