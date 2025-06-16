n = int(input()) # 설탕 키로
k = [5,3]
num = 0 # 봉지개수
dp = [float('inf')] * (n + 1)

for i in k:
    dp[0] = 0
    for j in range(1,n+1):
       if dp[j-i] + 1 < dp[j] : 
          dp[j] = dp[j-i]+1
       

if dp[n] == float('inf') : 
    print(-1)
else : 
    print(dp[n])
    