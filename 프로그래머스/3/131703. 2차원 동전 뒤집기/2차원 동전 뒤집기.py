from copy import deepcopy

def trans(map_, lev, col_n, row_n):
    if lev < col_n:
        map_col = deepcopy(map_)

        for row in range(row_n):
            map_col[row][lev] ^= 1

    return map_col

def solution(beginning, target):
    min_ans = float("inf")

    row_n = len(beginning)
    col_n = len(beginning[0])

    def dfs(map_, cost, lev):
        nonlocal min_ans
        
        if map_ == target:
            min_ans = min(min_ans, cost)
            return

        if cost >= min_ans:
            return

        if lev >= row_n and lev >= col_n:
            return
                
        # 뒤집지 않는 경우
        dfs(map_, cost, lev + 1)

        # lev번째 행만 뒤집는 경우
        if lev < row_n:
            map_row = deepcopy(map_)

            for col in range(col_n):
                map_row[lev][col] ^= 1

            dfs(map_row, cost + 1, lev + 1)
        
        return

    no_set = set()
    yes_set = set()
    
    for i in range(col_n):
        if beginning[0][i] == target[0][i]:
            no_set.add(i)
        else:
            yes_set.add(i)
            
    map_1 = deepcopy(beginning)
    map_2 = deepcopy(beginning)
    
    for yes in yes_set:
        map_1 = trans(map_1, yes, col_n,row_n)
            
    for no in no_set:
        map_2= trans(map_2, no, col_n,row_n)

    for col in range(col_n):
        map_2[0][col] ^= 1

    dfs(map_1, 0+len(yes_set), 1)
    dfs(map_2, 1+len(no_set), 1)
    
    return -1 if min_ans == float("inf") else min_ans