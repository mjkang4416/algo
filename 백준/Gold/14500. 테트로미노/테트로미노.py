import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False] * m for _ in range(n)]
max_result = 0

def dfs(x,y,cnt,result):
    global answer

    if cnt ==4:
        answer = max(result,answer)
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,cnt+1,result+arr[nx][ny])
            visited[nx][ny] = False

def remain(x,y):
    remain =[]
    global remain_answer
    cur = arr[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            remain.append(arr[nx][ny])
    if len(remain) == 4:
        remain.remove(min(remain))
        remain_answer = max(remain_answer, sum(remain)+cur)
    elif len(remain) == 3:
        remain_answer = max(remain_answer,sum(remain)+cur)
    return

for i in range(n): # bfs 로 가능한것
    for j in range(m):
        visited[i][j] = True
        answer = 0
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False
        max_result = max(max_result,answer)


for i in range(n):
    for j in range(m):
        remain_answer = 0
        remain(i, j)
        max_result = max(max_result,remain_answer)

print(max_result)