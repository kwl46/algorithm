import sys
input = sys.stdin.readline

N = int(input())

str_lst =  list()

for i in range(N):
    s =str(input().strip())
    str_lst.append(s)

dict_lst = dict()
ans_tuple = ()
max_similar = 0

for i in range(len(str_lst)):
    s = str_lst[i]
    temp_s = ""
    cnt = 0
    for c in s:
        temp_s += c
        cnt += 1
        if temp_s in dict_lst:
            if cnt >= max_similar:
                if ans_tuple != ():
                    if cnt == max_similar:
                        if ans_tuple[0] > dict_lst[temp_s]:
                            ans_tuple = (dict_lst[temp_s], i)
                            max_similar = cnt
                    else:
                        ans_tuple = (dict_lst[temp_s], i)
                        max_similar = cnt
                else:
                    ans_tuple = (dict_lst[temp_s], i)
                    max_similar = cnt
        else:
            dict_lst[temp_s] = i

if ans_tuple != ():
    print(str_lst[ans_tuple[0]])
    print(str_lst[ans_tuple[1]])
else:
    print(str_lst[0])
    print(str_lst[1])