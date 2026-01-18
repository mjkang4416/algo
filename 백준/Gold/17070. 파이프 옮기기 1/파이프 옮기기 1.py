import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp= [[[0]*n for _ in range(n)] for _ in range(3)]
dp[0][0][1] =1 #가로로 올때 x,y
for i in range(2,n):
    if arr[0][i] == 0: #첫줄은 가로 밀기만 가능
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1,n):
    for j in range(1,n):
        if arr[i][j] == 0 and arr[i][j-1] ==0 and arr[i-1][j]== 0:
            dp[2][i][j] = dp[1][i-1][j-1] + dp[2][i-1][j-1] +dp[0][i-1][j-1]
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] +dp[2][i][j-1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
print(dp[0][n - 1][n - 1] + dp[1][n - 1][n - 1] + dp[2][n - 1][n - 1])