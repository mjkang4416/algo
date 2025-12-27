import sys
from collections import deque
input= sys.stdin.readline

n,m = map(int,input().split()) #사다리수, 뱀수
up = deque()
down = []
visited = [False for _ in range(101)] #한번 방문한 숫자는 bfs 하면서 재방문 할 필요 없음

#뱀,사다리 넣기
for i in range(n+m):
    x,y = map(int,input().split())
    if i>=n:
        down.append((x,y)) #x 번 칸에 도착하면 y 번 칸으로 이동해라
    else:
        up.append((x,y))

def bfs(point,cnt):
    q = deque()
    q.append((point,cnt))
    while q:
        now = q.popleft()
        po = now[0]
        cnt = now[1]

        if po == 100:
            print(cnt)
            return

        for i in range(1,7):
            point = po +i
            if point >100 or visited[point]: #100보다 크거나 방문한거면 continue
                continue

            for j in range(len(down)):
                if point == down[j][0] and not visited[point]:  #down 이랑 마주치고 방문 안된거면
                    point = down[j][1]
                    visited[point] = True #방문처리
                    q.append((point,cnt+1))

            for k in range(len(up)):
                if point == up[k][0] and not visited[point]:  #up 이랑 마주치고 방문 안된거면
                    point = up[k][1]
                    visited[point] = True #방문처리
                    q.append((point,cnt+1))

            if not visited[point]: # 둘중 아무랑도 안마주친거면
                visited[point] = True
                q.append((point,cnt+1))

bfs(1,0)