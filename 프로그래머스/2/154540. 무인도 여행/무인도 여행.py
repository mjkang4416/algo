from collections import deque
#x 바다, 숫자 문인도 , 상화좌우 연결되는거 하나 땅 => 이거 합한 값 식량 => 머무를 수 있는 시간, 
#각 섬에서 최대 몇일 머무를 수 있는지 오름차순 정렬후 return 
#지낼곳 없음 -1 
 

def Dfs(x,y,map_list,dx,dy):
    
    re = 0
    arr = deque() #덱으로 스텍 구현
    arr.append((x,y)) #첫노드 
    
    while arr:
        now_nod = arr.pop() # 매번 하나씩 뽑아서 
        
        x = now_nod[0]
        y = now_nod[1]
        
        if map_list[x][y] == 'X':
            continue
        
        re += int(map_list[x][y]) #더한다음 
        map_list[x][y] = 'X' # x 처리 
        
        for i in range(4): #해당 노드에서 갈수 있는길 append 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(map_list) and 0 <= ny < len(map_list[0]) and map_list[nx][ny]!='X':
                arr.append((nx,ny))
    return re
    
def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    answer = [] #정답배열
    map_list = [[0] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)): #문자열 때서 복사한 배열 
        for j in range(len(maps[i])):
            map_list[i][j] = maps[i][j]
    
    for i in range(len(map_list)):
        for j in range(len(map_list[i])): 
            result = 0
            if map_list[i][j] != 'X': #X 가 아닌곳 완탐
                result = Dfs(i,j,map_list,dx,dy)
                if result != 0:
                    answer.append(result)
                    
    if len(answer) != 0 :
        answer.sort()
        return answer
    else :
        return [-1]

   