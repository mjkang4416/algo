import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split()) #수빈, 동생 위치
#수빈 x-1, x+1 ,2*x 1초 후 이동가능
#수빈이가 동생 찾을수 있는 가장 빠른 시간이 몇 초 후인지
dx = [-1,1,2]
visited = [False]*(100001)
def bfs(point,cnt):

    q = deque()
    q.append((point,cnt))
    while q:
        now = q.popleft()
        point = now[0]
        cnt = now[1]
        if point == k:
            print(cnt)
            break

        for i in (point-1,point+1,point*2):
                if 0<=i<=100000 and not visited[i]:
                    visited[i] = True
                    q.append((i,cnt+1))



bfs(n,0)