import sys
from collections import deque
input = sys.stdin.readline
n,m,v = map(int,input().split()) #정점개수,간선개수,탐색시작할 정점 번호
#간선 양방향
arr = [[] for _ in range(n+1)]

def dfs(now):
    for i in arr[now]:
        if i not in visited:
            visited.append(i)
            dfs(i)

def bfs():
    q = deque()
    visited = [0]
    visited[0] = v
    q.append(v)

    while q :

        now = q.popleft()

        for i in arr[now]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    return visited

for _ in range(m): #양방향 그래프 만들어주기
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
    arr[a].sort()
    arr[b].sort()

q = deque()
visited = [0]
visited[0]=v
q.append(v)
dfs(v)
print(' '.join(map(str,visited)))

print(' '.join(map(str,bfs())))
