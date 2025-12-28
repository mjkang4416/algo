import sys
from collections import deque

input = sys.stdin.readline
result = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#0 아닌경우 이동 가능
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr[i][j] = int(arr[i][j])

def dfs(x,y,cnt):
    q = deque()
    q.append((x,y))
    while q:
        now = q.pop()
        x = now[0]
        y = now[1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] != 0:
                arr[nx][ny] = 0
                cnt+=1
                q.append((nx,ny))
    return cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] !=0 :
            arr[i][j] = 0
            result.append(dfs(i,j,1))

print(len(result))
result.sort()
for i in result:
    print(i)