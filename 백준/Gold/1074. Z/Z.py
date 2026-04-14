import sys
input = sys.stdin.readline

N, R, C = map(int ,input().split())

min_v = 0
sum_v = 0
arr = [[1,2],[3,4]]
def dfs(r,c, n):
    global min_v, sum_v

    if n == 1:
        
        sum_v = arr[r][c]
        return
    
    mid_r = ((2**n)//2)-1
    mid_c = ((2**n)//2)-1

    if r <= mid_r and c <= mid_c:
        min_v += 0
        dfs(r,c,n-1)
    elif r <= mid_r and c > mid_c:

        min_v += ((2**n)*(2**n))//4
        dfs(r,c-mid_c-1,n-1)
    elif r > mid_r and c <= mid_c:
        min_v += ((2**n)*(2**n))//2
        dfs(r-mid_r-1,c,n-1)
    else:
        min_v += ((2**n)*(2**n))//4*3
        dfs(r-mid_r-1,c-mid_c-1,n-1)

dfs(R,C,N)

print(min_v-1+sum_v)