import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort() #1 1 2 2 5
result = []
i = 0
while i<n:
    temp = arr[i:i+arr[i]]
    result.append(temp)
    i+=arr[i]
print(len(result))