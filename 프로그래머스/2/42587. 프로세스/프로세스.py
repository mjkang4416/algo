from  collections import deque

def solution(priorities, location):
    #특정 프로세스 몇번째로 실행되는지 
    #pop -> 우선 순위 높은거 있으면 다시 넣음 
    #없으면 실행하고 종료 
    answer = 0
    qu = deque()
    for i in range(len(priorities)):
        qu.append(priorities[i])
    
    while qu :
        now = qu[0]
        size_chaeck = False
        for i in range(len(qu)):
            if now < qu[i]: #지금 뽑은거보다 큰게 있는 경우 
                size_chaeck = True
                
        if size_chaeck:
            qu.rotate(-1)
        else : # 큰게 없는 경우 
            if location == 0:
                return answer+1 #pop 
            pop_nod = qu.popleft()
            answer+=1
                
        if location != 0: #현재 위치 
                location-=1
        else : location = len(qu)-1
    
    return answer