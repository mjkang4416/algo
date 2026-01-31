import sys
input = sys.stdin.readline

st = input().rstrip()
bumm = input().rstrip()
stack = []
n = len(bumm)

for i in st:
    if len(stack)>=n and stack[-1] == bumm[-1]:
        is_true = True 
        for j in range(n): #4 개 검사했는데 다른게 있으면 계속 진행, 아니면 pop
            if stack[len(stack)-j-1] != bumm[n-j-1]:
                is_true = False #다른게 있는경우 
                break
        if is_true :
            for _ in range(n):
                stack.pop()


    stack.append(i)       

if len(stack)>=n and stack[-1] == bumm[-1]:
    is_true = True 
    for j in range(n): #4 개 검사했는데 다른게 있으면 계속 진행, 아니면 pop
        if stack[len(stack)-j-1] != bumm[n-j-1]:
            is_true = False #다른게 있는경우 
            break
    if is_true :
        for _ in range(n):
            stack.pop()

if len(stack):
    for i in stack:
        print(i,end="")
else:
    print("FRULA")