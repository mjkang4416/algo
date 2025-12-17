import itertools 

def solution(k, dungeons):
    arr = list(itertools.permutations(dungeons,len(dungeons)))
    answer = -1
    for min_arr in arr:
        result = 0 #가능한 던전 탐험 개수 
        temp = k
        for ar in min_arr :
            if temp >= ar[0] :
                result+=1
                temp-= ar[1]
        answer = max(answer,result)
    
    return answer