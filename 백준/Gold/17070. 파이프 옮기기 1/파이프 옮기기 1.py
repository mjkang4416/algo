import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


def to_row(x2,y2):
    if x2 + 1 < n and arr[x2 + 1][y2] == 0 :
        dfs(x2, y2, x2 + 1, y2)
    return

# 가로이동
def to_column(x2,y2):
    if y2 + 1 < n and arr[x2][y2 + 1] == 0 :
        dfs(x2, y2, x2, y2 + 1)
    return


def to_side(x2,y2):
    if y2 + 1 < n and x2 + 1 < n and arr[x2 + 1][y2 + 1] == 0:
        if  arr[x2][y2 + 1] == 0 and arr[x2 + 1][y2] == 0:
            dfs(x2, y2, x2 + 1, y2 + 1)
    return


def dfs(x1, y1, x2, y2):
    global cnt
    if x2 == (n-1) and y2 == (n-1):
        cnt += 1
        return

    #가로인경우
    if x1 == x2 and y1 != y2:
        #가로이동
        to_column(x2,y2)
        #대각선이동
        to_side(x2, y2)
    #세로인경우
    if x1 != x2 and y1 == y2:
        # 세로이동
        to_row(x2, y2)
        # 대각선이동
        to_side(x2, y2)
    #대각선인 경우
    if x1 != x2 and y1 != y2:
        # 가로이동
        to_column(x2, y2)
        # 세로이동
        to_row(x2, y2)
        # 대각선이동
        to_side(x2, y2)

dfs(0,0,0,1)
print(cnt)