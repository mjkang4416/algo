import sys

input = sys.stdin.readline

n = int(input())
arr = [0]*(n+1)
for i in range(1,n+1):
    arr[i] = int(input())
dp = [0]*(n+1) #n 번째 계단까지 올라왔을떄 최대 점수

if n ==1:
    print(arr[1])
elif n==2:
    print(arr[1]+arr[2])
else:
    dp[1] = arr[1]  # 첫계단 무조건 밟음
    dp[2] = arr[1] + arr[2]  # 두번째까지는 연속 가능
    dp[3] = max(arr[2]+arr[3],arr[1]+arr[3])
    for i in range(4,n+1):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
    print(dp[n])