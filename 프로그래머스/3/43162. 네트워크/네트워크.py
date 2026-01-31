def solution(n, computers):
    answer = 0
    parents = [i for i in range(n)]
    rank = [0] * (n+1)
    def find(a):
        if parents[a] == a:
            return a
        
        parents[a] = find(parents[a])
        return parents[a]
    
    def union(a,b):
        a = find(a)
        b = find(b)
        
        if rank[a] < rank[b]:
            parents[b] = a
        elif rank[b] < rank[a]:
            parents[a] = b
        else:
            parents[b] = a
            rank[a] += 1
    
    for i in range(len(computers)):
        computer = computers[i]
        for j in range(len(computer)):
            if computer[j] == 1:
                union(i,j)

    ans = set()
    for i in range(n):
        ans.add(find(i))

    answer = len(ans)

    return answer