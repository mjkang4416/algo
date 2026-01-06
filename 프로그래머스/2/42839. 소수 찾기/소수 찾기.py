from itertools import permutations
from collections import deque

def solution(numbers):
    answer = 0
    result = set()
    temp =[]
    
    
    for i in range(1,len(numbers)+1): 
        temp.extend(permutations(numbers,i)) #순열만들기
        result = set(int(''.join(i)) for i in temp)
    
    
    for i in result:
        is_not_sosu = False
        if i==1 or i==0 :
            continue
        for j in range(2,i//2+1): #소수검사
            if i%j==0:
                is_not_sosu = True
        if not is_not_sosu:
            answer+=1
    
    return answer
    
   