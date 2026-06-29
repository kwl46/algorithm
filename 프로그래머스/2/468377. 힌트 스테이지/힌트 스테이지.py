def solution(cost, hint):
    answer = 100000000000000
    n = len(cost)
    h_n = len(hint)
    h_dict = dict()
    
    for i in range(n+1):
        h_dict[i] = 0
    
    def dfs(stage_lev, hint_dict, sum_cost):
        nonlocal cost, hint, answer

        if stage_lev == n:
            answer = min(answer, sum_cost)
            return
        
        if hint_dict[stage_lev+1] >= len(cost[stage_lev])-1:
            sum_cost = sum_cost + cost[stage_lev][-1]
        else:
            sum_cost = sum_cost + cost[stage_lev][hint_dict[stage_lev+1]]
        
        if stage_lev < n-1:
            temp_dict = dict()
            
            for i in range(n+1):
                temp_dict[i] = hint_dict[i]
                
            for i in range(1, len(hint[stage_lev])):
                temp_dict[hint[stage_lev][i]] += 1
                
            dfs(stage_lev+1, temp_dict, sum_cost + hint[stage_lev][0])
            
        dfs(stage_lev+1, hint_dict, sum_cost)
        
            
        return

    dfs(0, h_dict, 0)
        
    return answer