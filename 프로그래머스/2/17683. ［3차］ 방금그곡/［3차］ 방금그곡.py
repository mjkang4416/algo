from collections import deque

def solution(m, musicinfos):
    #처음과 끝부분 이어서 재생된 멜로디 ㅇ
    #중간에 음악 끊을 경우, 원본에는 있는데 그곡이 안들은 곡일수도
    #조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 
    #재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
    #조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
    new_musicinfos = []
    result = []
    m_stack = []
    idx =0
    #m #처리
    for i in m:
        if i.isalpha():
            m_stack.append(i)
        elif i=='#':
            top = m_stack.pop()
            now = top+i
            m_stack.append(now)
    #musicinfos split 처리 
    for mu in musicinfos:
        new_musicinfos.append(mu.split(','))
    
    #받은 곡 처리 
    for first_time,last_time,name,mel in new_musicinfos:
        first_hour,first_minute = first_time.split(':')
        last_hour,last_minute = last_time.split(':')
    
        time = (int(last_hour)*60+int(last_minute))-(int(first_hour)*60+int(first_minute))
        
        #mel 받은거 #처리
        mel_stack = deque()
        for i in mel:
            if i.isalpha():
                mel_stack.append(i)
            elif i=='#':
                top = mel_stack.pop()
                now = top+i
                mel_stack.append(now)
        
        result_mel = []
        
        if len(mel_stack) < time: #멜로디가 시간보다 작을 경우 
            result_mel += mel_stack 
            for _ in range(time-len(mel_stack)): #시간만큼 돌린 멜로디 
                result_mel.append(mel_stack[0])
                temp = mel_stack.popleft()
                mel_stack.append(temp)
        else: 
            for i in range(time):
                result_mel.append(mel_stack[0])
                temp = mel_stack.popleft()
                mel_stack.append(temp)

        # return result_mel,m_stack
        #문자열 비교 
        for i in range(len(result_mel)-len(m_stack)+1):
            not_in = True
            for j in range(len(m_stack)):
                if m_stack[j] != result_mel[i+j]: #하나라도 다르면 false 
                    not_in = False
            if not_in: #전부다 같을때 
                result.append((name,time,idx))
                idx+=1
                break
                
    result.sort(key = lambda x:(-x[1],x[2]))

    if len(result)>=1:
        return result[0][0]
    elif len(result)==0: return "(None)"