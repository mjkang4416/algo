from collections import deque

def solution(s):
    answer = 0
    qu = deque()
    for st in s:
        qu.append(st)
        
    for i in range(len(qu)):
        if i != 0:
            qu.rotate(-1)
        stack = []
        correct = True
        for j in range(len(qu)):
            if qu[j] == '{' or qu[j] == '(' or qu[j] == '[':
                stack.append(qu[j])
            else :
                if len(stack) == 0:
                    correct = False
                    break 
                now = stack.pop()
                if now == '{' and qu[j] != '}':
                    correct = False
                    break 
                elif now == '(' and qu[j] != ')':
                    correct = False
                    break 
                elif now == '[' and qu[j] != ']':
                    correct = False
                    break 
        if correct and len(stack) == 0:
            answer+=1
    
    return answer