import heapq

push = heapq.heappush
pop = heapq.heappop

def convert_time(time):
    h = int(time[0:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:8])
    
    return int(h + m + s)

def deconvert_time(time):
    h = time // 3600
    m = (time % (3600)) // 60
    s = time - (m*60) - (h*3600)
    
    str_h = str(h)
    str_m = str(m)
    str_s = str(s)
    
    if len(str_h) < 2:
        str_h = "0" + str_h
    if len(str_m) < 2:
        str_m = "0" + str_m
    if len(str_s) < 2:
        str_s = "0" + str_s
        
    return str_h + ":" + str_m + ":" + str_s
    
def solution(play_time, adv_time, logs):
    answer = ''
    
    play_t = convert_time(play_time)
    adv_t = convert_time(adv_time)
    
    if play_t <= adv_t:
        return "00:00:00"
    
    hq = []
    
    logs_lst = []
    
    for i in range(len(logs)):
        s_time = logs[i][0:8]
        e_time = logs[i][9:]

        s_t = convert_time(s_time)
        e_t = convert_time(e_time)
        
        logs_lst.append((s_t, e_t))
    
    logs_lst.append((play_t, play_t+1))
    logs_lst.sort()
    
    ans_lst = []
    v = 0
    
    for i in range(len(logs_lst)):
        s_time = logs_lst[i][0]
        e_time = logs_lst[i][1]
        ans_lst.append((v, len(hq)))
        
        while hq:
            if s_time >= hq[0]:
                t = pop(hq)
                ans_lst.append((t,len(hq)))
                v = t
            else:
                break
        v = s_time
        
        push(hq, e_time)
    
    map_lst = [0] * (play_t+1)
    
    before = 0
    cnt = 0
    
    for i in range(1, len(ans_lst)):
        for j in range(before, ans_lst[i][0]):
            map_lst[j] = cnt
        
        before = ans_lst[i][0]
        cnt = ans_lst[i][1]
        
        
    start = 0
    cur = sum(map_lst[:adv_t])
    max_v = cur

    for i in range(1, play_t - adv_t + 1):
        cur -= map_lst[i - 1]
        cur += map_lst[i + adv_t - 1]

        if max_v < cur:
            start = i
            max_v = cur
    
    answer = deconvert_time(start)

    return answer