import sys
input = sys.stdin.readline

def dfs(point,now_node,visited):
    for i in result[now_node]: #현재 노드가 방문 가능한 애들 구함
        if not visited[i] :
            result_list[point][i]= 1
            visited[i] = True
            dfs(point,i,visited)



n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
result = [[] for i in range(n)] #인접 list 로
result_list = [[0]*n  for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            result[i].append(j)


for i in range(len(result)):
    visited = [False]*n
    dfs(i,i,visited)

for i in range(len(result_list)):
    for j in range(len(result_list)):
        print(result_list[i][j],end=" ")
    print()