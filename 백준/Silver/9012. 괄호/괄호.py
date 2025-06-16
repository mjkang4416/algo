n = int(input())
arr = []
PsStack =[]

for i in range(n):
    arr.append(input())

for j in range(n):
    PsStack =[]
    for k in range(len(arr[j])):
        safe = True
        if arr[j][k] == '(':
            PsStack.append(arr[j][k])
        elif arr[j][k] == ')': 
            if not PsStack: # ) 가 왔는데 스택이 빈 경우
                safe = False
                break
            else:
                PsStack.pop()
    if not PsStack and safe == True : # 스택에 남은 (가 없고 break 되지 않은경우 
        print("YES") 
    else: 
        print("NO") 