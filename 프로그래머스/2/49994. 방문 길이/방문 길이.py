def solution(dirs):
    answer = 0
    commnd = {'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}
    visited = set()
    x = 0
    y = 0
    for co in dirs:
        nx = x+commnd[co][0]
        ny = y+commnd[co][1]
        if -5<= nx <= 5 and -5<= ny <= 5 :
            visited.add(((x,y),(nx,ny)))
            visited.add(((nx,ny),(x,y)))
            x = nx
            y = ny
    answer = len(visited)//2
    return answer