import sys
input = sys.stdin.readline

N, M, S, T = map(int,input().split())

map_lst = [[float("inf")] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int,input().split())
    map_lst[a][b] = min(map_lst[a][b], c)

for i in range(1, N+1):
    map_lst[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        if map_lst[i][k] == float("inf"):
            continue
        for j in range(1, N+1):
            if i == j:
                map_lst[i][j] = 0
                continue
            map_lst[i][j] = min(map_lst[i][j], map_lst[i][k]+map_lst[k][j])

Q = int(input())

n = map_lst[S][T]

for i in range(Q):
    a1,b1,c1,a2,b2,c2 = map(int,input().split())
    n1 = map_lst[S][a1] + map_lst[b1][T] + c1
    n2 = map_lst[S][a2] + map_lst[b2][T] + c2
    n3 = map_lst[S][a1] + c1 + map_lst[b1][a2] + c2 + map_lst[b2][T]
    n4 = map_lst[S][a2] + map_lst[b2][a1] + map_lst[b1][T] + c1 + c2

    ans = min(n,n1,n2,n3,n4)
    if ans == float("inf"):
        ans = -1
    print(ans)