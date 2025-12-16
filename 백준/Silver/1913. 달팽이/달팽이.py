n = int(input())
point = int(input())
arr = [[0]*n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

num = (n*n)

point_x = 0
point_y = 0

x = 0
y = 0

arr[x][y] = num
idx = 0

while True:
    if num == point:
        point_x = x + 1
        point_y = y + 1

    if num == 1 :
        break
    if n > x+dx[idx] >= 0 and n > y+dy[idx] >= 0 and arr[x+dx[idx]][y+dy[idx]] == 0 :
        x += dx[idx]
        y += dy[idx]
        num-=1
        arr[x][y] = num
    else: idx = (idx+1)%4

for ar in arr:
    for i in ar:
        print(i,end=" ")
    print()
print(point_x,point_y)



