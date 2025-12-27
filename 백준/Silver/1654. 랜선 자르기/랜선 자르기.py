import sys
input = sys.stdin.readline

k,n = map(int,input().split())
arr= []
for _ in range(k):
    arr.append(int(input()))
start,end = 1,max(arr)

while start <= end:
    mid =(start+end)//2

    line = 0
    for i in arr:
        line+=i//mid

    if line >= n:
        start = mid+1
    else:
        end = mid-1
print(end)
