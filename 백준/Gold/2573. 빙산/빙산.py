from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

map_lst = []

for i in range(N):
    map_lst.append(list(map(int, input().split())))

start = tuple()
dr = [1,0,-1,0]
dc = [0,1,0,-1]
leng = 0

dq = deque()
start = tuple()

for i in range(N):
    for j in range(M):
        if map_lst[i][j] != 0:
            leng += 1
            start = (i,j)

time = 0
flag = True

while True:
    if leng == 0:
        break
    time += 1
    dq.append(start)
    check_set = set()
    check_set.add(start)
    cnt = 0
    mm = 0

    while dq:
        r, c = dq.popleft()
        cnt += 1

        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]

            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
                continue
            if (next_r, next_c) in check_set:
                continue
            if map_lst[next_r][next_c] == 0:
                if map_lst[r][c] > 0:
                    map_lst[r][c] -= 1
                    if map_lst[r][c] == 0:
                        mm += 1
                continue
            
            dq.append((next_r,next_c))
            check_set.add((next_r,next_c))
        
        if map_lst[r][c] != 0:
            start = (r,c)

    if cnt != leng:
        flag = False
        break
    else:
        leng -= mm



if flag:
    print(0)
else:
    print(time-1)