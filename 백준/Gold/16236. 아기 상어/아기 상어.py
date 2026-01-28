from collections import deque
import sys

input = sys.stdin.readline

s_x = 0
s_y = 0
s_size = 2  # 초기2
time = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
equal_size_cnt = 0
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 아기상어 위치 구하기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            s_x = i
            s_y = j
            arr[i][j] = 0

# 1 개수 세는 함수
def count():
    fish = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != 9:
                fish.append((i, j))
    return fish

# 이동하는 함수
def bfs():
    q = deque()
    q.append((0,s_x, s_y))
    visited = [[False] * n for _ in range(n)]
    candidate = []
    while q:  # 들어올 수 있는애 계산
        t,x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and s_size >= arr[nx][ny] and not visited[nx][ny]:
                # 1초에 상하좌우 한칸씩 이동
                visited[nx][ny] = True
                if 0 < arr[nx][ny] < s_size:
                    candidate.append((t+1,nx, ny))

                q.append((t+1,nx, ny))

    candidate.sort()

    return candidate


while True:
    result = bfs()
    if len(result) == 0:  # 먹을 수 있는거 없으면
        break

    t, x, y= bfs()[0]

    time += t
    s_x = x
    s_y = y
    arr[x][y] = 0

    equal_size_cnt += 1
    # 상어 넓이 증가
    if equal_size_cnt == s_size:
        equal_size_cnt = 0
        s_size += 1

print(time)