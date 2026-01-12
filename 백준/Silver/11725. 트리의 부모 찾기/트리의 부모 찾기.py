import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
linked_list = [[] for _ in range(n+1)]
linked_list[0].append(1)
for i in range(n-1):
    a,b = map(int,input().split())
    linked_list[a].append(b)
    linked_list[b].append(a)


visited = [False for _ in range(n+1)]
visited[0] = True

result =[0 for _ in range(n+1)]

def dfs(node):
    for i in linked_list[node]:
        if not visited[i]:# 해당 노드에 방문한 적이 없으면 이전이 부모노드 (깊이우선 탐색이니까)
            result[i] = node
            visited[i] = True
            dfs(i)


dfs(1)

for i in range(2,n+1):
    print(result[i])