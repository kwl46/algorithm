def solution(genres, plays):
    answer = []
    
    dict_lst = dict()
    
    for g in genres:
        dict_lst[g] = [0]
    
    for i in range(len(plays)):
        dict_lst[genres[i]][0] += plays[i]
        dict_lst[genres[i]].append((plays[i],i))

    sort_lst = []

    for key in dict_lst:
        sort_lst.append((dict_lst[key][0], key))
    
    sort_lst.sort(reverse=True)
    
    for s, k in sort_lst:
        temp_lst = dict_lst[k][1:]
        temp_lst.sort(key=lambda x:(-x[0],x[1]))
        cnt = 0
        for p, i in temp_lst:
            cnt += 1
            answer.append(i)
            if cnt == 2:
                break
    
    return answer