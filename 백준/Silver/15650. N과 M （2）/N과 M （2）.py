import sys
input = sys.stdin.readline

n,m =map(int,input().split())
arr = [i for i in range(1,n+1)]

def dfs(start,result):
    if len(result)==m:
        print(*result)
        return

    for i in range(start,n):
        result.append(arr[i])
        dfs(i+1,result)
        result.pop()


dfs(0,[])