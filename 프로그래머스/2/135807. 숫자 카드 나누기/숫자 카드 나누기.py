def solution(arrayA, arrayB):
    answer = 0
    #둘중 하나 만족하는 가장 큰 양의 정수 찾기
    #A 를 모두 나눌 수 있고 , B를 하나도 못나눔
    #B 를 모두 나눌 수 있고 , A를 하나도 못나눔
    
    gdgA = arrayA[0]
    gdgB = arrayB[0]
    
    def gdg(i,gdg_n):
        if i%gdg_n == 0: #나누어 떨어지면 그대로 reuturn
            return gdg_n
        return gdg(gdg_n,i%gdg_n) #gdgA 수정
        
    def isDiv(gdg_n,arr):
        for i in arr:
            if i%gdg_n == 0:
                return False
        return True
    
    for i in arrayA[1:]:
        gdgA = gdg(i,gdgA) #새로 들어오는 애랑 현재 애랑 비교 
    for i in arrayB[1:]:
        gdgB = gdg(i,gdgB) #새로 들어오는 애랑 현재 애랑 비교 
    
    if isDiv(gdgA,arrayB):
        answer = max(gdgA,answer)
    if isDiv(gdgB,arrayA):
        answer = max(gdgB,answer)
    return answer