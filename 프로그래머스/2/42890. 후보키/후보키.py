from collections import defaultdict
from itertools import combinations
def solution(relation):
    # 가로로 만들수 있는 조합 인덱스로 구하기 
    # 겹치는 조합 있는지 
    # 더 작은 개수로 되는지 
    combi = []
    for i in range(1,len(relation[0])+1):
        combi.extend(combinations(range(len(relation[0])),i)) #0~가로개수 까지 배열 i 개 조합

    unique = []  
    for idx in combi: #선택된 col 조합에 해당하는 튜플 만듬
        tupl = [tuple(item[j] for j in idx) for item in relation] #하나 행 뽑아서 조합된 인덱스 가져옴 
        
        if len(relation) == len(set(tupl)): #유일성
            is_only = True
            for x in unique:
                if set(x).issubset(set(idx)):
                    is_only = False
                    break
            if is_only:
                unique.append(idx)
            
    return len(unique)