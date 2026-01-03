import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(n)]
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

p_cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            q.append((i,j)) #현재위치

while q:
    now = q.popleft()
    x = now[0]
    y = now[1]

    for i in range(4):
        nx= x+dx[i]
        ny= y+dy[i]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] != 'X':
            if arr[nx][ny] == 'P':
                p_cnt+=1

            arr[nx][ny] = 'X' #방문처리
            q.append((nx,ny))

if p_cnt == 0:
    print("TT")
else:
    print(p_cnt)

