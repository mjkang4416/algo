import sys
from collections import deque

input = sys.stdin.readline


def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((x,y))
    while q:
        now = q.popleft()
        x = now[0]
        y = now[1]

        for i in  range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1:
                arr[nx][ny] =0 #방문처리
                q.append((nx,ny))

T = int(input())

for _ in range(T):
    m,n,k = map(int,input().split()) #가로,세로,배추개수
    arr = [[0]*m for _ in range(n)]
    answer = 0

    for _ in range(k): #qu 에 배추 있는 노드 넣기
        y,x = map(int,input().split())
        arr[x][y] =1

    for i in range(n): #bfs
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = 0 #방문처리
                bfs(i,j)
                answer +=1

    print(answer)