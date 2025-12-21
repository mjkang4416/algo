import sys

input = sys.stdin.readline
num = 0
while True:
    n = int(input())
    arr = []

    if n == 0:
        break

    for i in range(n):
        arr.append(input().rstrip())
    arr.sort()
    num+=1
    print(num)
    for st in arr:
        print(st)
