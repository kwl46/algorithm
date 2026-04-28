def solution(tickets):
    answer = []
    
    dict_lst = dict()
    check_lst = dict()
    
    for t in tickets:
        s = t[0]
        d = t[1]
        
        if s not in dict_lst:
            dict_lst[s] = []
        
        dict_lst[s].append(d)
        
    for key in dict_lst:
        dict_lst[key].sort()
        check_lst[key] = [False] * len(dict_lst[key])
    
    flag = False
    
    def dfs(loc, ways):
        nonlocal answer, tickets, flag
        if flag:
            return
        
        if len(ways) == len(tickets)+1:
            answer = ways
            flag = True
            return
        
        if loc not in dict_lst:
            return
        
        for i in range(len(dict_lst[loc])):
            if check_lst[loc][i]:
                continue
            check_lst[loc][i] = True
            dfs(dict_lst[loc][i], ways+[dict_lst[loc][i]])
            check_lst[loc][i] = False
        
        return
    
    dfs("ICN", ["ICN"])
    
    return answer