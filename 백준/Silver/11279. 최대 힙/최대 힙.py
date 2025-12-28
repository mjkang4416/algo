import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
hq =[]
for _ in range(n):
    arr.append(int(input()))

for i in arr:
    if i == 0 :
        if len(hq):
            print(-heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq,-i)
