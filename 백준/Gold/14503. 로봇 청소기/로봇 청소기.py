# 상하좌우중 청소안된칸 있으면 90 도로 회전 -> 해당 칸이면 이동 -> 청소 
# 상하좌우 중 청소안된칸 없으면 후진 (백트레킹 , 방향 유지한채로) -> 상하좌우 보면서 반복
# 백트레킹 불가하면 작동 멈춤 (벽일 경우)
# 방향 0북 1동 2남 3서 
# arr 0 인 경우 청소 안된거 , 1 인 경우 벽 

n,m = map(int, input().split())
r,c,d = map(int, input().split()) #r 세로 c 가로 d 방향 

arr = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1] 


#방문 배열 
visited = [[False]*m for _ in range(n)]

sum = 1
visited[r][c] = True
            
def dfs(x,y,d):
    global sum 
    flag = False

    if arr[x][y] != 1 and visited[x][y] != True :
        sum+=1
        visited[x][y] = True
  
    # 상하좌우중 갈 방향 있는 경우 
    for _ in range(4) :
            d = (d+3)%4 #90 도 회전 
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >=0 and nx <n and ny >=0 and ny <m : #상하좌우 범위 체크 
                if arr[nx][ny] != 1 and visited[nx][ny] != True : #상하좌우가 벽이 아니고 방문되지 않은거면 
                    dfs(nx,ny,d)
                    flag = True
                    break
                
    # 상하좌우중 갈 방향 없는 경우 
    if flag == False :
        if arr[x - dx[d]][y- dy[d]] == 1: #뒤쪽칸이 벽인경우  or visited[x - dx[d]][y- dy[d]] == True 
            return sum 
        else :
            dfs(x - dx[d],y- dy[d],d) #아닌경우 기존 d 유지
                    
     
dfs(r,c,d)
print(sum)