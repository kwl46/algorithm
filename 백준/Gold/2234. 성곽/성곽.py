from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int,input().split())

map_lst = []

for i in range(N):
    map_lst.append(list(map(int,input().split())))

n_lst = [8,4,2,1]
dr = [1,0,-1,0]
dc = [0,1,0,-1]

dq = deque()

check = [[0] * M for _ in range(N)]
max_room = 0
room_cnt = 0

size_dict = dict()

for i in range(N):
    for j in range(M):
        if check[i][j] > 0:
            continue
        room_cnt += 1
        check[i][j] = room_cnt
        room_size = 0
        dq.append((i,j))

        while dq:
            r, c = dq.popleft()
            room_size += 1
            n = map_lst[r][c]
            
            for k in range(4):
                next_r = r + dr[k]
                next_c = c + dc[k]
                
                if (n - n_lst[k]) < 0:
                    if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
                        continue
                    if check[next_r][next_c] > 0:
                        continue
                    check[next_r][next_c] = room_cnt
                    dq.append((next_r, next_c))
                else:
                    n -= n_lst[k]
        
        size_dict[room_cnt] = room_size
        max_room = max(max_room, room_size)

s_max = 0

for i in range(N):
    for j in range(M):
        pos_spec = check[i][j]

        for k in range(4):
            next_r = i + dr[k]
            next_c = j + dc[k]
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
                continue
            if check[next_r][next_c] == pos_spec:
                continue
            s_max = max(s_max, size_dict[check[next_r][next_c]] + size_dict[check[i][j]])

print(room_cnt)
print(max_room)
print(s_max)