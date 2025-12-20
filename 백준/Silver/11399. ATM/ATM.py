import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split())) #인출하는데 걸리는 시간
arr.sort()

result = 0
answer = 0
for i in range(n):
    result+=arr[i]
    answer+=result

print(answer)