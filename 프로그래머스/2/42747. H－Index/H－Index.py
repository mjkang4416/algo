def solution(citations):
    for i in range(len(citations),0,-1): #5,4,3,2,1 
        types = 0
        for j in range(len(citations)):
            if citations[j] >= i: #값이 index 보다 크거나 같
                types +=1 #해당 논문 포함
        if types >= i: 
            return i
    return 0