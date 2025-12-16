#캐시 크기에 따른 실행시간 측정
#cacheSize 캐시 크기
#cities 도시 이름
#영문자, 대소문 구별 x 
#도시이름 순서대로 처리할때 총 실행시간 
#가장 덜 최근에 사용된 애 케시에서 뺌 -> priority queue 
#캐시에 있으면 1, 없으면 5 실행시간 
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    qu = deque() 
    
    for citie in cities : #도시 배열 순회 
        citie = citie.lower()
        #qu에 없는경우 
        if citie not in qu :
            answer+=5
        #qu에 있는 경우 
        else :
            answer +=1 
            
        #큐 관리 
        if len(qu) == cacheSize: #3개가 다 찼고 큐에 있는 경우 
            if citie in qu: #큐에 있는 경우 
                qu.remove(citie)
                qu.append(citie)
            elif qu : #큐에 없는 경우 
                qu.popleft()
                qu.append(citie) 
        else : #3개가 안찼을때 
            if citie in qu : #큐에 있는 경우 
                qu.remove(citie)
                qu.append(citie)
            else :
                qu.append(citie)  #큐에 없는 경우 
            

    return answer