from collections import deque
#x 바다, 숫자 문인도 , 상화좌우 연결되는거 하나 땅 => 이거 합한 값 식량 => 머무를 수 있는 시간, 
#각 섬에서 최대 몇일 머무를 수 있는지 오름차순 정렬후 return 
#지낼곳 없음 -1 

def solution(maps):
    arr = [list(i) for i in maps]
    result = []
    n = len(arr)
    m = len(arr[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y,cnt):
        q = deque()
        q.append((x,y))
        arr[x][y] = 'X'
        while q:
            x,y = q.popleft()

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<m and arr[nx][ny] != 'X':
                    q.append((nx,ny))
                    cnt+= int(arr[nx][ny])
                    arr[nx][ny] = 'X'
                    
        result.append(cnt)
            
    for i in range(n):
        for j in range(m):
            if arr[i][j] !='X':
                cnt = int(arr[i][j])
                bfs(i,j,cnt)
    if result:      
        return sorted(result)
    else :
        return [-1]