import heapq

push = heapq.heappush
pop = heapq.heappop

def solution(n, paths, gates, summits):
    answer = []
    
    map_lst = [[] for _ in range(n+1)]
    
    for i in range(len(paths)):
        map_lst[paths[i][0]].append((paths[i][1], paths[i][2]))
        map_lst[paths[i][1]].append((paths[i][0], paths[i][2]))
    
    check = [float("inf")] * (n+1)
    
    hq = []
    
    summits_set = set(summits)
    
    for i in range(len(gates)):
        push(hq, (0, gates[i]))
        check[gates[i]] = 0
    
    ans_int = float("inf")
    ans_sum = []
    
    while hq:
        inten, pos = pop(hq)
        
        if inten > ans_int:
            continue
        
        if pos in summits_set:
            ans_int = min(ans_int, inten)
            ans_sum.append(pos)
            continue
        
        for des, cost in map_lst[pos]:
            max_cost = max(inten, cost)
            if check[des] <= max_cost:
                continue
            check[des] = max_cost
            push(hq, (max_cost, des))
    
    ans_sum.sort()
    answer.append(ans_sum[0])
    answer.append(ans_int)
    
    return answer