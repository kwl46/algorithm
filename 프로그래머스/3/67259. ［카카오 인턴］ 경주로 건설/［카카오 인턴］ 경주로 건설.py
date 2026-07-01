from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    
    check = [[[float("inf")] * 4 for _ in range(M)] for _ in range(N)]
    
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    dq = deque()
    
    dq.append((0,0,0,0))
    dq.append((0,0,0,1))
    dq.append((0,0,0,2))
    dq.append((0,0,0,3))
    check[0][0][0] = 0
    check[0][0][1] = 0
    check[0][0][2] = 0
    check[0][0][3] = 0
    
    while dq:
        r, c, cost, direc = dq.popleft()
        
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
            next_cost = 0
            
            if direc == i:
                next_cost = cost + 100
            else:
                next_cost = cost + 600
                
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
                continue
            if board[next_r][next_c] == 1:
                continue
            if check[next_r][next_c][i] <= next_cost:
                continue
            
            check[next_r][next_c][i] = next_cost
            dq.append((next_r, next_c,next_cost,i))
    
    answer = min(check[-1][-1])
    
    return answer