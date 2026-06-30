def solution(n, s, a, b, fares):
    answer = 0
    map_lst = [[float("inf")] * (n+1) for _ in range((n+1))]
    
    for fare in fares:
        map_lst[fare[0]][fare[1]] = fare[2]
        map_lst[fare[1]][fare[0]] = fare[2]
    
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j:
                    map_lst[i][j] = 0
                    continue
                
                map_lst[i][j] = min(map_lst[i][j], map_lst[i][k] + map_lst[k][j])
    
    min_value = map_lst[s][a] + map_lst[s][b]
    
    for i in range(1, n+1):
        min_value = min(min_value, map_lst[s][i] + map_lst[i][a] + map_lst[i][b])
            
    answer = min_value
    return answer