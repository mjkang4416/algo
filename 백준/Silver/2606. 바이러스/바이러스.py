import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) #노드수
m = int(input()) #간선수
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)


result = set()

def dfs(now):
    global result

    result.add(now)
    
    for i in range(len(arr[now])):
        if arr[now][i] not in result:
            result.add(arr[now][i])
            dfs(arr[now][i])

dfs(1)
print(len(result)-1)
