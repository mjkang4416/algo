import math

k_cout = 0
def solution(n, k):
    #n명의 사람 줄세우는 순열 
    #사람 나열하는 방법 사전순으로 나열했을때 k 번째 방법
    arr =[i for i in range(1,n+1)]
    result = []
    
    for i in range(1,n+1):
        permu = math.factorial(n-i) #해당 자리에서 나오는 묶음 
        index = k//permu #두묶음 나옴 
        if k%permu == 0: #나누어 떨어지는 경우 
            index -=1 #인덱스를 하나 돌려줘서 숫자 -- 
            
        result.append(arr[index]) 
        arr.pop(index)
        k-=index*permu
    
    return result