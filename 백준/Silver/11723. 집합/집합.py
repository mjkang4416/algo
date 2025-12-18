import copy
import sys
input = sys.stdin.readline

n = int(input())

result = set()
for _ in range(n):
    arr = list(input().split())
    if arr[0] == "add":
        result.add(int(arr[1]))
    elif arr[0] == "remove":
        if int(arr[1]) in result:
            result.remove(int(arr[1]))
    elif arr[0] == "check":
        if int(arr[1]) in result :
            print(1)
        else :
            print(0)
    elif arr[0] == "toggle":
        if int(arr[1]) in result :
            result.remove(int(arr[1]))
        else :
            result.add(int(arr[1]))
    elif arr[0] == "all":
        result = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif arr[0] == "empty":
        result = set()