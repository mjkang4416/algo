import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())  #줄 개수, 합 구해야 하는 횟수
arr = list(map(int,input().split()))
sum_list = []
sum_list.append(arr[0])
for i in range(1,n): #구간합 구해놓기
    sum_list.append(sum_list[i-1]+arr[i])

for i in range(m):
    start,end=map(int,input().split())
    if start == 1:
        print(sum_list[end-1])
    else: print(sum_list[end-1]-sum_list[start-2])

