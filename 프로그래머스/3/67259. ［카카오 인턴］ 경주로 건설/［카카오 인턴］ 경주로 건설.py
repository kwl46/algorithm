import heapq
push = heapq.heappush
pop = heapq.heappop

def solution(board):
    N = len(board)
    M = len(board[0])
    
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    
    hq = []
    
    check = [[[float("inf")] * 4 for _ in range(M)] for _ in range(N)]

    push(hq, (0, (0,0), 0))
    push(hq, (0, (0,0), 1))
    push(hq, (0, (0,0), 2))
    push(hq, (0, (0,0), 3))
    
    check[0][0][0] = 0
    check[0][0][1] = 0
    check[0][0][2] = 0
    check[0][0][3] = 0
    answer = float("inf")
    
    while hq:
        cost, pos, direc = pop(hq)
        r = pos[0]
        c = pos[1]
        
        if r == N-1 and c == M-1:
            answer = min(answer,cost)
            
            
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
            
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
                continue
            if board[next_r][next_c] == 1:
                continue
                
            if i == direc:
                new_cost = cost + 100
                if check[next_r][next_c][i] < new_cost:
                    continue
                check[next_r][next_c][i] = new_cost
                push(hq, (new_cost, (next_r,next_c), i))
            else:
                new_cost = cost + 600
                if check[next_r][next_c][i] < new_cost:
                    continue
                check[next_r][next_c][i] = new_cost
                push(hq, (new_cost, (next_r,next_c), i))

    return answer