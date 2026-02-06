def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:(x[0],x[1]-x[0]))
    left = routes[0][0]
    right = routes[0][1]
    cnt = 1
    
    for i in range(1, len(routes)):
        if routes[i][1] <= right:
            left = routes[i][0]
            right = routes[i][1]
            continue
        if routes[i][0] > right:
            left = routes[i][0]
            right = routes[i][1]
            cnt += 1
            continue
    
    answer = cnt
    return answer