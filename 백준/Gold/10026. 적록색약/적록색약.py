import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
img = [list(input().rstrip()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#적록 색약이 아닌사람이 봤을때
def bfs_nomal(x,y):
    while q1:
        now = q1.popleft()
        x = now[0]
        y = now[1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and img[nx][ny] == img[x][y] and visited1[nx][ny]==False:
                q1.append((nx,ny))
                visited1[nx][ny] = True



#적록 색약인 사람이 봤을때
def bfs_not_color(x,y):
    while q2:
        now = q2.popleft()
        x = now[0]
        y = now[1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and img[nx][ny] and not visited2[nx][ny]:
                if img[nx][ny] == img[x][y] or ((img[nx][ny] =='R' and img[x][y]=='G') or (img[nx][ny] =='G' and img[x][y]=='R')):
                    q2.append((nx,ny))
                    visited2[nx][ny] = True

q1 = deque()
q2 = deque()
visited1 = [[False]*n for _ in range(n)]
visited2 = [[False]*n for _ in range(n)]
result1 = 0
result2 = 0

for i in range(0,n):
    for j in range(0,n):
        if not visited1[i][j]:
            q1.append((i, j))
            visited1[i][j] = True
            bfs_nomal(i, j)
            result1+=1
        if not visited2[i][j]:
            q2.append((i, j))
            visited2[i][j] = True
            bfs_not_color(i,j)
            result2+=1

print(result1,result2)