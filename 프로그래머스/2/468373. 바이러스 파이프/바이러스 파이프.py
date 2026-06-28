from collections import deque

def solution(n, infection, edges, k):
    answer = 0
    
    map_lst = [[] for _ in range(n+1)]
    
    for i in range(len(edges)):
        map_lst[edges[i][0]].append((edges[i][1], edges[i][2]))
        map_lst[edges[i][1]].append((edges[i][0], edges[i][2]))
    
    def dfs(lev, virous,before):
        nonlocal answer, k

        if lev == k:
            answer = max(answer, len(virous))
            return
            
        for i in range(1,4):
            dq = deque()
            for v in virous:
                dq.append(v)
            tmp_virous = set()
            while dq:
                pos = dq.popleft()

                for des, typ in map_lst[pos]:
                    if des in virous:
                        continue
                    if des in tmp_virous:
                        continue
                    if i != typ:
                        continue
                    else:
                        tmp_virous.add(des)
                        dq.append(des)

            for v in virous:
                tmp_virous.add(v)
            dfs(lev+1, tmp_virous, i)
            
    dfs(0, {infection},0)
    
    return answer