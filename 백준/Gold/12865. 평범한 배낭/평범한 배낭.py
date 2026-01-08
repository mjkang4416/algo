import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [(0,0)]
for i in range(1,n+1):
    w,v = map(int,input().split())
    arr.append((w,v))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1): #현재까지 온 물건 번호
    w,v = arr[i]
    for j in range(1,k+1): #현재 고려중인 무게
        if j >=w : #현재 무게가 해당 무게보다 작거나 같은 경우
            dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-w]+v)
        else : #현재 무게가 k 보다 클때 , 못넣음
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) #해당무게를 물건하나를 덜 고려한 상태로 만든거 vs 해당무게 -1을 해당 물건 개수로 만든거
print(dp[n][k])