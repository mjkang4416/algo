import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
hq = []
for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    if arr[i] == 0:
        if len(hq) ==0:
            print(0)
        else:print(heapq.heappop(hq)[1])
    else:
        if arr[i] <0 :
            heapq.heappush(hq,(-arr[i],arr[i]))
        else:
            heapq.heappush(hq, (arr[i],arr[i]))