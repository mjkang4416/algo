from collections import deque

def solution(bridge_length, weight, truck_weights): #다리길이 , 견딜무게, 트럭들
    #모든 트럭이 다리 건너려면 최소 몇초 ? 
    answer = 0
    
    bridge = [0 for _ in range(bridge_length)] #다리 길이만큼 배열
    bridge = deque(bridge)
    
    
    truck_weights = deque(truck_weights)
    curr_weight = 0 #현재 다리위에 있는 트럭 무게합
    
    time = 0
    
    while truck_weights: #마지막 트럭이 다리에 올라갈때 까지만 시뮬 
        #한칸이동 -> 다리에서 무게 빼기
        time+=1 
        curr_weight-= bridge.popleft() 
        
        if curr_weight+truck_weights[0] >weight:
            bridge.append(0) #무게땜에 더 못넣을때 0 으로 배열 개수 유지
        else : # 넣을 수 있을때 
            curr_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())     
    time+= bridge_length #마지막 트럭 빠져나가야 하니까 
    return time