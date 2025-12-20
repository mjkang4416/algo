from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,maps):
    global dx
    global dy
    qu = deque()
    qu.append((x,y))
    n = len(maps)
    m = len(maps[0])
    
    while qu: 
        now = qu.popleft()
        
        for i in range(4):
            nx = now[0]+dx[i] #x
            ny = now[1]+dy[i] #y 좌료 
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] += maps[now[0]][now[1]] 
                    qu.append((nx,ny)) #좌료 qu에 
                       
    if maps[n-1][m-1] == 1:
        return -1
    else :
        return maps[n-1][m-1]
    
def solution(maps):
    answer = bfs(0,0,maps)

    return answer