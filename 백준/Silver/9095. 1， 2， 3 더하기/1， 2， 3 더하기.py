import sys

input = sys.stdin.readline

T = int(input())

def dfs(num):
    global result

    if num == 0:
        result+=1
        return
    if num < 0:
        return

    dfs(num-1)
    dfs(num-2)
    dfs(num-3)

for _ in range(T):
    num = int(input())
    result=0
    dfs(num)
    print(result)
