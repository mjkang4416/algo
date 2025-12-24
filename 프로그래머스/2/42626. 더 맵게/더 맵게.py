import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    cnt = 0
    while heap[0] < K:
        if len(heap)==0 or len(heap)==1:
            return -1
    
        sco = heapq.heappop(heap) + (heapq.heappop(heap)*2)
        heapq.heappush(heap,sco)
        cnt+=1
        
    return cnt