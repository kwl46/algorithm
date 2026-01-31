import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())

map_lst = []

for i in range(N):
    map_lst.append(list(map(int, input().split())))

dr = [1,0,-1,0]
dc = [0,1,0,-1]

check = [[-1] * (N+1) for _ in range(N+1)]

def dfs(r,c):
    sum_v = 1
    max_len = 0
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]

        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N:
            continue
        if map_lst[r][c] >= map_lst[next_r][next_c]:
            continue
        if check[next_r][next_c] > -1:
            max_len = max(max_len, check[next_r][next_c])
            continue
        max_len = max(max_len, dfs(next_r, next_c))
    
    check[r][c] = sum_v + max_len

    return check[r][c]

max_v = 0

for i in range(N):
    for j in range(N):
        if check[i][j] > -1:
            max_v = max(max_v, check[i][j])
            continue
        dfs(i,j)
        max_v = max(max_v, check[i][j])

print(max_v)