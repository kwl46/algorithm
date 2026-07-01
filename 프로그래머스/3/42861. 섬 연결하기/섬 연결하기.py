import heapq

push = heapq.heappush
pop = heapq.heappop

def solution(n, costs):
    answer = 0
    
    map_lst = [[] for _ in range(n)]
    
    for cost in costs:
        map_lst[cost[0]].append((cost[1], cost[2]))
        map_lst[cost[1]].append((cost[0], cost[2]))
    
    hq = []
    
    push(hq, (0, 0))
    check = [False] * n
    
    while hq:
        cost, pos = pop(hq)
        
        if check[pos]:
            continue
        
        answer += cost
        
        check[pos] = True
        
        for des, cost in map_lst[pos]:
            if check[des]:
                continue
            push(hq, (cost, des))
        
    return answer