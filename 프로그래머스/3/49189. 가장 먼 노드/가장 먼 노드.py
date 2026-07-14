from collections import deque

def solution(n, edge):
    answer = 0
    
    map_lst = [[] for _ in range(n+1)]
    
    for i in range(len(edge)):
        map_lst[edge[i][0]].append(edge[i][1])
        map_lst[edge[i][1]].append(edge[i][0])
    
    check = [False] * (n+1)
    check[1] = True
    dist_lst = [0] * (n+1)
    
    dq = deque()
    dq.append((1,0))
    
    max_cost = 0
    
    while dq:
        pos, cost = dq.popleft()

        max_cost = max(max_cost, cost)
        
        dist_lst[pos] = cost
        
        for des in map_lst[pos]:
            next_cost = cost + 1
            if check[des]:
                continue
            
            check[des] = True
            
            dq.append((des, next_cost))
    
    for d in dist_lst:
        if d == max_cost:
            answer += 1
    
    return answer