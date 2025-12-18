#각 종류별로 최대 1가지만 착용 가능 
#착용 의상 완전히 겹치지 않으면 다른 착장이라 취급
#최소 하루에 한개의 착장 입음
#서로 다른옷 조합 reutrun 
import itertools
from math import prod

def solution(clothes):
    answer = 1
    dic = {}
    result = []
    
    for types in clothes: #딕셔너리에 값 추가 
        if types[1] in dic:
            dic[types[1]] +=1
        else : dic[types[1]] = 1
        
    arr = [value for value in dic.values()]
    
    for i in range(len(arr)):
        answer *= (arr[i]+1)

    
    return answer-1