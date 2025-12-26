def solution(skill, skill_trees): 
    #가능한 스킬트리 개수 , 가능한 모든 경우의수
    #스킬 순서, 스킬트리 순서는 문자열로
    answer = 0
    for arr in skill_trees:
        st =''
        for i in arr:
            if i in skill:
                st+=i
        if st == skill[:len(st)]:
            answer+=1
                    
    return answer