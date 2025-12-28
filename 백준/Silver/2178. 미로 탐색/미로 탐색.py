import sys
from collections import deque

input = sys.stdin.readline

#1 이동가능
#1,1출발
#n,m 도착하는 최소칸
#시작,도착위치 포함
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,arr):
    q = deque()
    q.append((x,y))
    global n,m
    while q:
        now = q.popleft()
        x = now[0]
        y = now[1]

        if x == n-1 and y == m-1:
            print(arr[x][y])
            return


        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1:
                arr[nx][ny] += arr[x][y]
                q.append((nx,ny))




n,m = map(int,input().split()) #세로,가로
arr = [list(input().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        arr[i][j] = int(arr[i][j])

bfs(0,0,arr)