from collections import deque

def solution(queue1, queue2):
    answer = -2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    cnt = 0
    
    while True:
        
        if cnt >= 10**6 :
            return -1
            exit(0)
        
        if sum1 < sum2:
            num = queue2.popleft()
            queue1.append(num)
            cnt+=1
            sum1 += num
            sum2 -= num
        elif sum1 > sum2 :
            num = queue1.popleft()
            queue2.append(num)
            cnt+=1
            sum2 += num
            sum1 -= num
        elif sum1 == sum2:
            return cnt
            exit(0)