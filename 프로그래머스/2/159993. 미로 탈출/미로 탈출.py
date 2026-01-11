from collections import deque

def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    arr = []

    for i in maps:
        arr.append(list(i))
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'S':
                start = [i,j]
            elif arr[i][j] =='E':
                exit = [i,j]
            elif arr[i][j] =='L':
                lab =[i,j]

    def bfs(x,y,point):
        global answer
        q = deque()
        q.append((x,y,0))
        visited = [[False]*len(arr[0]) for _ in range(len(arr))]
        visited[x][y] = True
        while q:
            x,y,num = q.popleft()
            
            if arr[x][y] == point:
                return num
                 
        
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<len(arr) and 0<=ny<len(arr[0]) and not visited[nx][ny] and arr[nx][ny]!='X':
                    visited[nx][ny] = True
                    q.append((nx,ny,num+1))
                
    
    exit_num = bfs(start[0],start[1],'L')
    lab_num  = bfs(lab[0],lab[1],'E')

    if not lab_num or not exit_num:
        return -1
        
    else :return int(lab_num+exit_num)