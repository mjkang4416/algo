from collections import deque

#세로,가로
n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]

visited = []
Rspotx = 0
Rspoty = 0
Bspotx = 0
Bspoty = 0

#왼오위아래 이동
dx = [-1,1,0,0]
dy = [0,0,1,-1]

#구슬 초기위치 
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            Rspotx = j
            Rspoty = i
        elif arr[i][j] == 'B':
            Bspotx = j
            Bspoty = i


def move(x,y,dx,dy) :
    cnt =0
    while arr[y+dy][x+dx] != '#' and arr[y][x] != 'O': #다음 이동에 문제가 없는 동안 
        x += dx 
        y += dy
        cnt+=1
    return x,y,cnt



def bfs(Rspotx ,
Rspoty,
Bspotx,
Bspoty) : 
    qu = deque()
    qu.append((Rspotx,Rspoty,Bspotx,Bspoty,1))
    visited.append((Rspotx,Rspoty,Bspotx,Bspoty)) #중복방문 방지 
    while qu :
        
        Rspotx,Rspoty,Bspotx,Bspoty,result = qu.popleft() # 튜플로 묶으면 이렇게 한번에 뺄수도 있구나 .. 

        if result >10 :
            break

        for i in range(4):
            Rx,Ry,Rcnt = move(Rspotx,Rspoty,dx[i],dy[i]) #R과 B 구슬 한쪽 방향으로 이동 
            Bx,By,Bcnt = move(Bspotx,Bspoty,dx[i],dy[i])

            if arr[By][Bx] == 'O': #파란 구슬이 구멍에 들어갈때 
                continue

            if arr[Ry][Rx] == 'O':
                print(result)
                return
            
            if By == Ry and Bx == Rx : #겹쳐진거라면 앞에서 출발한게 앞에오고 뒤에서 출발한게 뒤에와야 
                if Rcnt > Bcnt :
                    Rx -= dx[i]
                    Ry -= dy[i]
                else :
                    Bx -= dx[i]
                    By -= dy[i]

            if (Rx,Ry,Bx,By) not in visited :
                visited.append((Rx, Ry, Bx, By)) # 현재자리 방문 처리 
                qu.append((Rx,Ry,Bx,By,result+1)) # 위치 해당 자리로 바꿈 ( 큐에 넣음 )
    print(-1)

bfs(Rspotx,
Rspoty,
Bspotx,
Bspoty)