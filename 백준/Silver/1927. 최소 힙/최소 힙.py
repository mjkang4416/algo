import heapq
import sys
input = sys.stdin.readline

n = int(input())
hp = []

arr = []
for i in range(n):
    arr.append(int(input()))

for i in arr:
    if i == 0:
        if len(hp) != 0:
            print(heapq.heappop(hp))
        else:
            print(0)
    else:
        heapq.heappush(hp,i)
