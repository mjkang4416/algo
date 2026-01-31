import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(n)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])

visited = [[[False,0] for _ in range(m)] for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    cnt = 1
    q.append((0,0,0,cnt))
    visited[0][0][0] = True
    while q:
        x,y,wall,cnt = q.popleft()

        if x == n-1 and y == m-1:
            return cnt

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 0: #0일때 다 방문 가능
                    if not visited[nx][ny][wall]: #부수고 온 애가 방문되지 않았을 경우, (부수고 왔는지 안부수고 왔는지 모르니까()
                        q.append((nx,ny,wall,cnt+1))
                        visited[nx][ny][wall] = True
                else:
                    if wall == 0: #1인데 부수지 않았을 경우
                        if not visited[nx][ny][1]: #1인애를 방문 처리 해줌
                            q.append((nx,ny,1,cnt+1))
                            visited[nx][ny][1] = True

if n ==1:
    print(1)
else:
    result = bfs()
    if result:
        print(result)
    else:
        print(-1)