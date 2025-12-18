import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
unlisten = []
unseen =[]
for _ in range(n+m):
    arr.append(input())

for i in range(n):
    unlisten.append(arr[i])

for j in range(n,n+m):
    unseen.append(arr[j])

result = set(unlisten) & set(unseen)

print(len(result))
result = sorted(result)
for re in result:
    print(re,end="")
