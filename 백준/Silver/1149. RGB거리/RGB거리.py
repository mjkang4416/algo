import sys

input = sys.stdin.readline

n = int(input()) #집의개수

arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[float('inf')]*3 for _ in range(n)]

for i in range(3):
    dp[0][i] = arr[0][i]

for i in range(1,n):
    for j in range(3): #내가 이자리에 온거면 앞 뒤는 다른거어야
        if j==0:
            dp[i][j] = min(dp[i-1][j+1],dp[i-1][j+2])+arr[i][j]
        elif j==2:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j-2])+arr[i][j]
        else:
            dp[i][j] = min(dp[i - 1][j-1], dp[i-1][j+1])+arr[i][j]

print(min(dp[n-1]))