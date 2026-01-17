import heapq
def solution(n, k, enemy):
    answer = 0
    q = []
    round_cnt = 0
    for i in range(len(enemy)):
        heapq.heappush(q,enemy[i]) 
        not_k = True
        
        if len(q) > k:
            n-= heapq.heappop(q) #제일 작은거 뺌
                
        if n < 0:
            return i
            
    return len(enemy)