import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n_lst = []

while True:
    try:
        n_lst.append(int(input()))
    except:
        break

def dfs(s, e):
    if s > e:
        return
    mid = e + 1

    for i in range(s+1,e+1):
        if n_lst[i] > n_lst[s]:
            mid = i
            break

    dfs(s+1, mid-1)
    dfs(mid, e)
    print(n_lst[s])

dfs(0, len(n_lst)-1)