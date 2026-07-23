import math

def solution(arrayA, arrayB):
    answer = 0
    
    arrayA.sort()
    arrayB.sort()
    resultA = arrayA[0]
    
    for i in range(1, len(arrayA)):
        resultA = math.gcd(resultA, arrayA[i])
    
    resultB = arrayB[0]
    
    for i in range(1, len(arrayB)):
        resultB = math.gcd(resultB, arrayB[i])
    
    flag_A = True
    flag_B = True
    
    for i in range(len(arrayA)):
        if (arrayA[i] % resultB) == 0:
            flag_B = False
        if (arrayB[i] % resultA) == 0:
            flag_A = False
    
    if flag_A and flag_B:
        answer = max(resultA, resultB)
    elif flag_A:
        answer = resultA
    elif flag_B:
        answer = resultB
    else:
        answer = 0
        
    return answer