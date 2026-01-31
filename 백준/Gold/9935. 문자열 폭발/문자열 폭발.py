import sys
from collections import deque
input = sys.stdin.readline

origin_str = input().rstrip()
pop_str = list(input().rstrip())

n = len(origin_str)
pn = len(pop_str)
stack = []

for i in range(n):
    stack.append(origin_str[i])
  
    if stack[len(stack)-pn:len(stack)] == pop_str:
         for _ in range(pn):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")