from  collections import deque

n,k = map(int, input().split()) #n 배열개수 , k 종료횟수 

arr = deque(map(int, input().split())) 
robot = deque([0]*n) #어짜피 N 까지 돌면 빠지니까 최대 n 개만 잡아준다.
setpNum = 0

while True :

    setpNum +=1

    #한칸 회전 , 로봇과 가중치 이동 
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 #내리는 위치에 도달한 경우 내림 

    #한칸 이동 -> 내구도 1 빠짐
    for i in range(n-2,-1,-1): #내리기 바로 직전 위치부터 한칸씩 뒤로 가면서 0까지 
        if arr[i+1] >0 and robot[i+1] == 0 and robot[i] == 1:
            robot[i+1] = 1
            robot[i] = 0
            arr[i+1] -=1

    robot[-1] = 0 #내릴 위치에 있으면 내림

    # 올리는 위치에 로봇 올림 (0 아니고 해당 위치에 로봇 없으면 )
    if arr[0] != 0 and robot[0] == 0:
        robot[0] = 1
        arr[0] -= 1 

    #내구도 0 인거 k 개 이상이면 종료 
    if arr.count(0) >= k :
        break

print(setpNum)
