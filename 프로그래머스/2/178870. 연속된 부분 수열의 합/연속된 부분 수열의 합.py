def solution(sequence, k):
    #합이 K 인 부분수열
    #여러개인 경우 길이가 짧은거 
    #길이 짧은게 여러개면 시작 인덱스가 작은 수열
    #시작 인덱스와 마지막 인덱스 담아 return 
    answer = []
    
    end = 0
    sum_sequence = 0
    for i in range(len(sequence)): #start 포인터 증가 
        while sum_sequence < k and end < len(sequence): #k 보다 작은동안 
            sum_sequence+=sequence[end] #마지막 포인터 증가 
            end+=1
            
        if sum_sequence == k : #k 도달시
            answer.append([i,end-1,end-i+1]) #인덱스 집어넣음, 개수는 인덱스 차이로 
            sum_sequence-= sequence[i] # 전체 sum에서 start 빼줌
        elif sum_sequence > k:
            sum_sequence-= sequence[i]
            

    answer.sort(key=lambda x : (x[2],x[0]))
    result = []
    result.append(answer[0][0])
    result.append(answer[0][1])
    return result