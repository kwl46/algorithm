from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    map_lst = [[0] * 101 for _ in range(101)]
    
    for rec in rectangle:
        x1, y1, x2, y2 = rec
        
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if map_lst[i][j] == 2:
                    continue
                if i == x1 or j == y1 or i == x2 or j == y2:
                    map_lst[i][j] = 1
                else:
                    map_lst[i][j] = 2
        
        
    check = [[False] * 101 for _ in range(101)]
    
    dq = deque()
    dq.append((characterX,characterY,0))
    check[characterX][characterY] = True
    
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    
    while dq:
        r, c, cost = dq.popleft()
        
        if r == itemX and c == itemY:
            answer = cost//2
            break
        
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
            
            if next_r < 0 or next_r >= 101 or next_c < 0 or next_c >= 101:
                continue
            if check[next_r][next_c]:
                continue
            if map_lst[next_r][next_c] != 1:
                continue
            check[next_r][next_c] = True
            dq.append((next_r,next_c,cost+1))
        
    
    return answer