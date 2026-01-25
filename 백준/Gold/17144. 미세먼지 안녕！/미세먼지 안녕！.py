import sys
input = sys.stdin.readline
import copy
from collections import deque

#t초 지난 후 미세먼지 개수
#1초에 미세먼지 인접 4방향 확장
#확산되는 양은 (r,c)//5
#남은 미세먼지의 양은 (r,c) - ⌊(r,c)//5⌋×(확산된 방향의 개수)
#위쪽 공기청정기 반시계방향으로 순환 아래쪽 공기청정기 시계방향 순환
#바람이 불면 미세먼지가 방향대로 모두 한 칸씩 이동
#공기청정기로 들어간 미세먼지는 모두 정화

r,c,t = map(int, input().split()) #행,열,

arr = [list(map(int,input().split())) for _ in range(r)]
circular_arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            circular_arr.append((i, j))

#바이러스 확산
def virus():
    temp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            num = 0
            if arr[i][j] != -1 and arr[i][j] != 0:
                plus_num = arr[i][j] // 5
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<r and 0<=ny<c and arr[nx][ny]!=-1:
                        temp[nx][ny]+=plus_num
                        num+=1

                temp[i][j] += arr[i][j] - num*plus_num
    for x, y in circular_arr:
        temp[x][y] = -1
    return temp


#공기청정기 돌리기
def circulator(x,y,idx):
    if idx == 0: #반시계 방향 회전
        for i in range(x - 1, 0, -1):
            arr[i][0] = arr[i - 1][0]
        for j in range(c - 1):
            arr[0][j] = arr[0][j + 1]
        for i in range(x):
            arr[i][c - 1] = arr[i + 1][c - 1]
        for j in range(c - 1, 1, -1):
            arr[x][j] = arr[x][j - 1]

        arr[x][1] = 0
    elif idx == 1: #시계방향 회전
        for i in range(x + 1, r - 1):
            arr[i][0] = arr[i + 1][0]
        for i in range(c - 1):
            arr[r - 1][i] = arr[r - 1][i + 1]
        for i in range(r - 1, x, -1):
            arr[i][c - 1] = arr[i - 1][c - 1]
        for i in range(c - 1, 1, -1):
            arr[x][i] = arr[x][i - 1]

    arr[x][1] = 0

while t:
    t-=1
    #바이러스 찾아서 확산
    arr = virus()

    #공기순환
    for i in range(len(circular_arr)):
        circulator(circular_arr[i][0],circular_arr[i][1],i)


result = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != -1 and arr[i][j] !=0 :
            result += arr[i][j]
print(result)