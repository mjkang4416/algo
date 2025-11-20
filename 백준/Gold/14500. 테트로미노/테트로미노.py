# 1*1 사각형을 연결해서 도형을 만들어 봅시다
# 정사각형 겹치면 안되고, 다 연결 돼있어야 
# 변끼리 연결돼있어야! 꼭짓점 닫는건 안됨
# 종이 위에 하나 놓을건데 숫자 적혀있으니까 그거 최대 되도록 돌려서 테트리스 하셈

n,m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [ [False] * m for _ in range(n) ]

# 이동방향 
dx = [1,-1,0,0]
dy = [0,0,1,-1]

maximum = 0 #최댓값 저장 


def dfs(x,y,tmp,cnt):
    global maximum 
    if cnt == 4: #개수가 4개가 되면 더함 
        maximum = max(maximum,tmp)
        return #return 되야 해당 context 끝나고 다음거 실행되겠지 
    for i in range(4): #상하좌우 움직이면서 방문 
        if x+dx[i] >=0 and x+dx[i]<n and y+dy[i]>=0 and y+dy[i] < m : #범위 체크 
            if visited[x+dx[i]][y+dy[i]] == False :
                visited[x + dx[i]][y +dy[i]] = True #dx, dy 더한 위치에서 방문처리 , 백트레킹 위해 원본 그대로둠
                dfs(x+dx[i],y+dy[i],tmp + arr[x + dx[i]][y +dy[i]],cnt+1) #다음 상하좌우 체크 위해 
                visited[x + dx[i]][y +dy[i]] = False


def fy(x,y):
    global maximum
    tepArr = []
    for i in range(4):
        if  x+dx[i] >=0 and x+dx[i]<n and y+dy[i]>=0 and y+dy[i] < m :
            nx = x +dx[i]
            ny = y +dy[i]
            tepArr.append(arr[nx][ny])
    length = len(tepArr)
    if length == 4:
       tepArr.sort(reverse=True) #기본이 내림차순 
       tepArr.pop() #가장 작은거 뺌
       maximum = max(maximum,sum(tepArr)+arr[x][y])
    elif length == 3:
        maximum = max(maximum,sum(tepArr)+arr[x][y])
    return # 둘다 아니면 바로 return 해당 모양 만들어지지 않음. 


#대칭, 돌려가면서 전체 검사 
for i in range(n) : 
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,arr[i][j],1)
        visited[i][j] = False
        fy(i,j)
           
print(maximum)
        
