import sys
input = sys.stdin.readline


n = int(input()) #합이 n 이 되게하는 제곱수의 최소 개수
dp = [0]* (n+1) # 해당 숫자름 만들 수 있는 개수

k = 1
while k**2 <= n : #제곱수들 다 1 표기
    dp[k**2] = 1
    k+=1



for i in range(1,n+1):
    if dp[i] != 0: #제곱수면 계산안함
        continue
    j = 1
    while j**2<=i:
        if dp[i] ==0 :
            dp[i] = dp[j**2] + dp[i-j**2]
        else:
            dp[i] = min(dp[i],dp[j**2] + dp[i-j**2])
        j+=1
        
print(dp[n])




