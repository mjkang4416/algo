from collections import deque

def solution(order):
    #상자 1~n
    #1번부터 상자 내림
    #1번이 순서 안맞으면 스택에 넣음
    #스택 사용해도 순서 이상하면 더이상 상자 안싣음
    stack = []
    answer = 0
    num = 0
    idx = 0
    for i in range(len(order)):
        stack.append(i+1) #1부터 보조 컨테이너에 집어넣음

        #보조 컨테이너에 값이 있으면 계속 확인
        while stack:
            if stack[-1]==order[idx]: #해당 값이 order 과 일치하면 
                answer+=1
                idx+=1
                stack.pop()# 빼준다.
            else: # 일치하지 않는 경우 계속 쌓음
                break
    return answer