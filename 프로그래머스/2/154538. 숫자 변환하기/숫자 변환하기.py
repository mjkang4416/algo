from collections import deque
def solution(x, y, n):
    cnt=0
    
    q = deque()
    q.append((x,0))
    
    visited = set()
    visited.add(x)
    arr=[2,3,n]
    
    while q:
        now = q.popleft()
        x = now[0]
        cnt = now[1]
        if x == y :
            return cnt
            exit()
        for i in range(3):
            if i == 2:
                nx = x+arr[i]
            else:
                nx = x*arr[i]
            if nx <= y and nx not in visited:
                q.append((nx,cnt+1))
                visited.add(nx)
        
    return -1