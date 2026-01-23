import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

# 1-indexed 그래프
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

items = list(map(int, input().split()))

# 자기 자신 거리 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 🔥 간선 r개만 입력
for _ in range(r):
    a, b, d = map(int, input().split())
    graph[a][b] = d
    graph[b][a] = d

# 플로이드 와샬
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 각 시작점에서 아이템 수집
ans = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            tmp += items[j - 1]   # items는 0-indexed

    ans = max(ans, tmp)

print(ans)
