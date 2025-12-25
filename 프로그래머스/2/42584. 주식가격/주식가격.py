def solution(prices): #초단위로 기록된 가격
    #가격이 떨어지지 않은 기간은 몇초인지 
    n = len(prices)
    answer = [0]*n
    for i in range(n): #전체가 떨어지지 않을 경우로 초기화 
         answer[i] = n-i-1

    stack = []
    stack.append(0)
    for i in range(1,n): #현재 값
        while stack and prices[stack[-1]] > prices[i]: #- 만나는 순간
            now = stack.pop() # 쌓인 인덱스 값
            answer[now] = i-now #-- 되는 현재 인덱스 - 쌓인 인덱스 => 시간계산
        stack.append(i) #현재 인덱스 넣어주고 다시 쌓음

    return answer