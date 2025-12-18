def solution(topping):
    #공평하게 자르는 방법의 수 
    answer = 0
    
    dic = {}
    
    for i in range(len(topping)):
        if topping[i] in dic :
            dic[topping[i]] +=1
        else : dic[topping[i]]=1
    
    type = 0
    mydic = {}
    for i in range(len(topping)): #돌면서 종류 몇개 가질 수 있는지 확인
        if topping[i] not in mydic  : #..여기서 터지네
            mydic[topping[i]] = 1
            type+=1 #arr 에 없는 종류면 타입 증가
            
        dic[topping[i]]-=1 #dic 감소 

        if dic[topping[i]] == 0 :
            dic.pop(topping[i]) #0 되면 없앰
            
        if type == len(dic) : #남은타입과 내 type 개수 확인
            answer +=1 
        
    return answer