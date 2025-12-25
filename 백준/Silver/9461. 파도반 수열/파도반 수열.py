import sys
input = sys.stdin.readline
T = int(input())

arr = [1,1,1,2,2,3,4,5,7,9]

for i in range(5,96):
    arr.append(arr[i]+arr[-1])

for i in range(T):
    n = int(input())
    print(arr[n-1])