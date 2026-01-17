from collections import deque

min_cnt = 2e9

def solution(board):
    #부딧힐때까지 한방향으로 쭉 가는게 한번 이동 
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    bo = [list(board[i]) for i in range(len(board))]
    visited = [[False]*len(bo[0]) for _ in range(len(bo))]

    def bfs(s_x,s_y,cnt):
        q = deque()
        q.append((s_x,s_y,cnt))
        visited[s_x][s_y] = True
        while q:
            x,y,cnt = q.popleft()
            
            if bo[x][y] == 'G':
                return cnt

            for i in range(4):
                nx,ny = x,y
                while True:  #D 전까지 계속 미끄러짐 
                    nx += dx[i]
                    ny += dy[i]
                    if 0<=nx<len(bo) and 0<=ny<len(bo[0]):                   
                        if bo[nx][ny] == 'D':
                            nx-=dx[i]
                            ny-=dy[i]
                            break
                    else:
                        nx-=dx[i]
                        ny-=dy[i]
                        break
                            
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,cnt+1))
        return -1
    
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == "R":
                return bfs(i,j,0)
                break
                