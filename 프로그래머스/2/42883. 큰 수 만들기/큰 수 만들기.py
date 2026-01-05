def solution(number, k):
    #k 개 제거했을때 얻을 수 있는 가장 큰 수 하나 
    answer = []
    
    for i in range(len(number)):
        while answer and k>0 and int(answer[-1]) < int(number[i]) :
            answer.pop()
            k-=1
            
        answer.append(number[i])
        
    return ''.join(answer[:len(number)-k])
        