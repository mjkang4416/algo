#교집합의 크기/합집합의 크기
#a,b 가 공집합일 경우 1 
#다중집합 ok 교집합 = min(3,5)=1 3개 , 합집합 = max(3,5) 1 5개
import copy
 
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_list = []
    str2_list = []
    intersect = []
    
    #문자열 두개씩 쪼개서 넣기
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_list.append(str1[i:i+2])
    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_list.append(str2[i:i+2])
    
    temp = copy.deepcopy(str2_list)
    for st1 in str1_list: #교집합
        if st1 in temp:
            intersect.append(st1)
            temp.remove(st1)
    
    all_list = copy.deepcopy(str2_list)
    
    for st1 in str1_list: #합집합
        if st1 not in str2_list: 
            all_list.append(st1)
        else: 
            str2_list.remove(st1)

    #완성된 문자열이 0 일 경우 예외처리 
    if len(all_list)==0 :
        return 65536
    else : return int((len(intersect)/len(all_list))*65536)
    