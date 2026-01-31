import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = float('inf')
zero_arr= []
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

def combination(cnt,start):
    global answer
    if cnt ==3: #3개가 다 1이 되면 bfs 호출
        answer = min(bfs(),answer)
        return

    for i in range(start,len(zero_arr)):
        arr[zero_arr[i][0]][zero_arr[i][1]] = 1 #여기서 1로 만들어놓고
        combination(cnt+1,i+1)
        arr[zero_arr[i][0]][zero_arr[i][1]] = 0


def bfs():
    q = deque()
    visited = [[False] * m for _ in range(n)]
    two_num = 0
    for x,y in tow_arr:
        two_num+=1
        q.append((x,y)) #어짜피 visited 로 체크 해주기 때문에 한번에 넣어도 상관없음
    while q:
        x,y= q.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and arr[nx][ny] ==0:
                visited[nx][ny] = True
                two_num+=1
                q.append((nx,ny))
    return two_num

combination(0,0)
print(n*m-answer-one_num-3) #전체에서 2 개수 빼고,1개수 뺀거