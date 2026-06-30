def solution(n, times):
    answer = 0
    left = 0
    right = 100000000000000
    min_value = float("inf")
    
    while left < right:
        mid = (left + right) // 2
        sum_n = 0
        for time in times:
            sum_n += mid // time
        
        if sum_n < n:
            left = mid + 1
        else:
            right = mid
            min_value = min(min_value, mid)
    
    answer = min_value
    return answer