import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
answer = 0
rever_arr = arr[::-1]
increase = [1 for _ in range(n)]  # 해당 숫자까지 올때의 최댓값
decrease = [1 for _ in range(n)]
result = [0 for i in range(n)]
for i in range(n): #하나를 바이토닉 이라고 가정
    for j in range(i): #전체 다 구해두고 더할때는 i 기준으로 잘라서
        if arr[i] > arr[j] :
            increase[i] = max(increase[i],increase[j]+1)

        if rever_arr[i] > rever_arr[j]:
            decrease[i] = max(decrease[i],decrease[j]+1)

for i in range(n):
    result[i] = increase[i] + decrease[n-i-1]-1

print(max(result))