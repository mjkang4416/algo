from collections import deque

def solution(elements):
    
    #연속부분수열 1,2,3,... n 
    #1,1,4,9,7 => 2, 5,11,16,10 
    qu = deque()
    arr = []
    for el in elements: #큐에 넣기 
        qu.append(el)
    
    for i in range(len(elements)): # 연속 n 번 돌림
        num = 0
        for k in range(len(elements)): #n번 rotate 
            num+=qu[k]
            arr.append(sum(list(qu)[:i]))
            qu.rotate(-1)

        
    answer = list(set(arr))
    return len(answer)

