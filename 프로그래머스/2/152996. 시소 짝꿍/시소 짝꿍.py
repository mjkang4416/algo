from collections import Counter

def solution(weights):
    answer = 0
    #사람무게*축*좌석거리 양쪽 같으면 짝
    counter = Counter(weights)
    for t,v in counter.items():
        if v>=2:
            answer+= v*(v-1)//2 #같은숫자일 경우, 조합하는 수 구함
    
    weights = set(weights)
    for i in weights:
        if i*(2/3) in weights:
            answer += counter[i]*counter[i*(2/3)]
        if i*(2/4) in weights:
            answer += counter[i]*counter[i*(2/4)]
        if i*(3/4) in weights:
            answer += counter[i]*counter[i*(3/4)]

        
    return answer