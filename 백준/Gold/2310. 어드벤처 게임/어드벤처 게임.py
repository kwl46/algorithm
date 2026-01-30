from collections import deque
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    lst = [[]]

    for i in range(n):
        temp_lst = list(map(str, input().strip().split()))
        lst.append(temp_lst)

    dq = deque()
    dq.append((1, 0))
    check = [-1] * (n+1)
    check[1] = 0
    flag = False
    while dq:
        pos, money = dq.popleft()
        
        if pos == n:
            flag = True
            break

        for d in lst[pos][2:-1]:
            d= int(d)
            if lst[d][0] == "T":
                if money < int(lst[d][1]):
                    continue
                new_money = money -int(lst[d][1])
                if check[d] >= new_money:
                    continue
                check[d] = new_money
                dq.append((d, new_money))
            elif lst[d][0] == "L":
                if money < int(lst[d][1]):
                    new_money = int(lst[d][1])
                else:
                    new_money = money
                if check[d] >= new_money:
                    continue
                check[d] = new_money
                dq.append((d, new_money))
            else:
                if check[d] >= money:
                    continue
                check[d] = money
                dq.append((d, money))
    if flag:
        print("Yes")
    else:
        print("No")