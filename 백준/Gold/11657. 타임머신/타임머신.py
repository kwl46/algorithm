import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dist_lst = [float("inf")] * (N+1)
dist_lst[1] = 0
m_lst = []

for i in range(M):
    a, b, c = map(int,input().split())
    m_lst.append((a,b,c))

for i in range(N):
    updated = False

    for a,b,c in m_lst:
        if dist_lst[a] == float("inf"):
            continue
        if dist_lst[b] > dist_lst[a] + c:
            dist_lst[b] = dist_lst[a] + c
            updated = True
    if not updated:
        break

updated = False

for a,b,c in m_lst:
    if dist_lst[a] == float("inf"):
        continue
    if dist_lst[b] > dist_lst[a] + c:
        dist_lst[b] = dist_lst[a] + c
        updated = True

if updated:
    print(-1)
else:
    for i in range(2, len(dist_lst)):
        if dist_lst[i] == float("inf"):
            print(-1)
        else:
            print(dist_lst[i])
