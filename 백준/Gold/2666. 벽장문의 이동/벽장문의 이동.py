import sys

input = sys.stdin.readline

N = int(input())
x, y = map(int, input().split())

l = int(input())

uses = []

for i in range(l):
    uses.append(int(input()))

ans = float("inf")

def dfs(cost, n1, n2, target_index):
    global ans
    if target_index == l:
        ans = min(cost, ans)
        return
    if n1 == uses[target_index] or n2 == uses[target_index]:
        dfs(cost,n1,n2,target_index+1)
        return

    if n1 < uses[target_index] < n2:
        dfs(cost+(uses[target_index]-n1), uses[target_index], n2, target_index+1)
        dfs(cost+(n2-uses[target_index]), n1, uses[target_index], target_index+1)
        return
    if n1 > uses[target_index]:
        dfs(cost+(n1-uses[target_index]), uses[target_index], n2, target_index+1)
        return
    if n2 < uses[target_index]:
        dfs(cost+(uses[target_index]-n2), n1, uses[target_index], target_index+1)

dfs(0, x, y, 0)
print(ans)