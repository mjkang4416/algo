import copy

def solution(want, number, discount):
    #10일 동안 하나씩 가능
    answer = 0
    dic = {}
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        real_dic = copy.deepcopy(dic)
        for j in range(i,i+10):
            if discount[j] in real_dic:
                real_dic[discount[j]]-=1
                if real_dic[discount[j]] == 0:
                    real_dic.pop(discount[j])
        if len(real_dic) == 0:
            answer+=1
    return answer