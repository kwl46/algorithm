def solution(n, computers):
    answer = 0
    parents = [i for i in range(n)]
    
    def find(a):
        if parents[a] == a:
            return a
        
        parents[a] = find(parents[a])
        return parents[a]
    
    def union(a,b):
        a = find(a)
        b = find(b)
        
        if a < b:
            parents[b] = a
        else:
            parents[a] = b

    s = set()
    
    for i in range(len(computers)):
        computer = computers[i]
        for j in range(len(computer)):
            if computer[j] == 1:
                union(i,j)

    for i in range(n):
        find(i)
    
    for p in parents:
        s.add(p)
        
    answer = len(s)

    return answer