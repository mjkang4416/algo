import sys
input = sys.stdin.readline


t = int(input())
for i in range(t):
    n = int(input())
    arr = {}
    for i in range(n):
        name,type = input().rstrip().split()
        if type in arr:
            arr[type] +=1
        else:
            arr[type]=1
    result = 1
    for i in arr.keys():
        result*=(arr[i]+1)
    print(result-1)