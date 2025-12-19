import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dic ={}
commend = []
for i in range(n+m):
    if i < n:
        st = input()
        dic[st[:len(st)-1]] = i+1
    else :
        st = input()
        commend.append(st[:len(st)-1])

dic_list = list(dic)
for co in commend :
    if co.isdigit():
        print(dic_list[int(co)-1])
    else:
        print(dic[co])