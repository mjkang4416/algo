import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
one_result =0
zero_result =0
def dfs(x,y,n):
    global zero_result
    global one_result

    sub_arr = arr[x:x+n] #2차원 배열은 먼저 세로 슬라이싱 후 가로 슬라이싱 가능

    has_one = any(1 in row[y:y+n] for row  in sub_arr)
    has_zero = any(0 in row[y:y+n] for row in sub_arr)

    #각 사분면에 존재
    if has_one and has_zero:
        now = n // 2 #4개로 분할
        dfs(x, y, now)
        dfs(x, y + now, now)
        dfs(x + now, y, now)
        dfs(x + now, y + now, now)
    # 1만 존재
    elif has_one and not has_zero:
        one_result+=1
        return
    # 0만 존재
    elif not has_one and  has_zero:
        zero_result+=1
        return

# if any(1 in row for row in arr)and any(0 in row for row in arr):
#     dfs(0,0,n)
dfs(0,0,n)
print(zero_result)
print(one_result)