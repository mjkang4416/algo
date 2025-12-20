import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    commends = input().rstrip()
    n = int(input())
    arr= deque(input().rstrip().replace('[',"").replace(']',"").split(","))
    if n == 0:
        arr = deque()
    error_test = False
    reverse_test = False

    for commend in commends:
        if commend == 'R':
            if reverse_test:
                reverse_test = False
            else :reverse_test = True
        elif commend == 'D':
            if len(arr)!= 0:
                if reverse_test:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                error_test = True
    if error_test:
        print("error")
    else:
        if reverse_test:
            arr.reverse()
            print("[", end="")
            for i in range(len(arr)):
                if i == len(arr) - 1:
                    print(f"{arr[i]}", end="")
                else:print(f"{arr[i]},", end="")

            print("]")
        else:
            print("[", end="")
            for i in range(len(arr)):
                if i == len(arr) - 1:
                    print(f"{arr[i]}", end="")
                else:print(f"{arr[i]},", end="")
            print("]")
