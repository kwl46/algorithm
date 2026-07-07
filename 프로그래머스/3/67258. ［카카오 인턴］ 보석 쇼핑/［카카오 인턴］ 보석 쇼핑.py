def solution(gems):
    answer = [0,0]
    dict_lst = dict()
    
    for i in range(len(gems)):
        dict_lst[gems[i]] = 0
    
    left = 0
    right = 1
    min_value = float("inf")
    n = len(dict_lst)
    
    dict_lst[gems[left]] += 1
    cnt = 1
    
    while left < len(gems):
        if cnt < n:
            if right == len(gems):
                break
            if dict_lst[gems[right]] == 0:
                cnt += 1
            dict_lst[gems[right]] += 1
            right += 1
        else:
            if right - left < min_value:
                min_value = right - left
                answer = [left + 1, right]
                
            dict_lst[gems[left]] -= 1
            
            if dict_lst[gems[left]] == 0:
                cnt -= 1
            
            left += 1
            
    return answer