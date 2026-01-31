import sys
from collections import deque
import copy
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

zero_arr= []
comi_arr = []
tow_arr = []
one_num = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            zero_arr.append((i,j))
        if arr[i][j] == 2:
            tow_arr.append((i, j))
        if arr[i][j] == 1:
            one_num += 1

def combination(cnt,start,temp):
    if cnt ==3:
        comi_arr.append(list(temp))
        return

    for i in range(start,len(zero_arr)):
        temp.append(zero_arr[i])
        combination(cnt+1,i+1,temp)
        temp.pop()

combination(0,0,[])

def bfs(x,y,visited):
    q = deque()
    global two_num
    q.append((x,y)) #시작점2 에서 퍼지는거
    while q:
        x,y= q.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and arr[nx][ny] ==0:
                visited[nx][ny] = True
                two_num+=1
                q.append((nx,ny))

answer = float('inf')
for zero in comi_arr : #111 넣는 경우의수 반복
    for i in range(3):
        arr[zero[i][0]][zero[i][1]] =1
    two_num = 0
    visited = [[False] * m for _ in range(n)]
    for two in tow_arr: #2 퍼짐
        two_num+=1
        visited[two[0]][two[1]] = True
        bfs(two[0],two[1],visited)
    answer=min(answer,two_num)
    for i in range(3):
        arr[zero[i][0]][zero[i][1]] = 0
print(n*m-answer-one_num-3) #전체에서 2 개수 빼고,1개수 뺀거