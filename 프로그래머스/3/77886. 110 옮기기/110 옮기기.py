from collections import deque

def solution(s):
    answer = []
    
    for c in s:
        sum_v = 0
        
        dq = deque()
        
        for cc in c:
            dq.append(cc)
            if len(dq) > 2:
                if (dq[-3] + dq[-2] + dq[-1]) == "110":
                    sum_v += 1
                    dq.pop()
                    dq.pop()
                    dq.pop()
        
        c = "".join(list(dq))
        
        if c.find("11") != -1:
            index = c.find("11")
            ans = c[:index] + ("110" * sum_v) + c[index:]
        else:
            if c.rfind("0") != -1:
                index = c.rfind("0")
                ans = c[:index+1] + ("110" * sum_v) + c[index+1:]
            else:
                ans = ("110" * sum_v)+c

        answer.append(ans)
    
    return answer