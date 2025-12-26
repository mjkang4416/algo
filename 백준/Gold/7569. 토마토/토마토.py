import sys
from collections import deque

input = sys.stdin.readline
#위, 아래, 왼쪽, 오른쪽, 앞, 뒤 -> 하루가 지나면 익음 -> 몇일이면 다 익는지
#1 익, 0 안익, -1안들어있
m,n,h = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
zero_count = False
day = 0
q = deque()
def dfs():
    global h,day
    while q:
        now = q.popleft()
        now_h,x,y = now[0],now[1],now[2]

        #방문처리
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nh = now_h+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nh<h and arr[nh][nx][ny] == 0:
                arr[nh][nx][ny] = arr[now_h][x][y]+1
                q.append((nh,nx,ny))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i,j,k)) #h,x,y 값 넣는다.
dfs()


for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit(0)
        day = max(day,max(arr[i][j]))


print(day-1) #모두 1인 경우 0이 출력 
