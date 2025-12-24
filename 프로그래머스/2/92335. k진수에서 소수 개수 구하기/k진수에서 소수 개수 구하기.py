import math
def solution(n, k):
    answer = -1
    arr = ""
    while n != 0:
        remain = n%k
        n//=k
        arr+=str(remain)

    split_arr = arr[::-1].split('0')
    sum =0
    for i in split_arr:
        if len(i) == 0: #빈공간인 경우 
            continue
        if int(i)<2:
            continue
        sosu = False
        for j in range(2,int(math.sqrt(int(i)))+1):
            if int(i)%j == 0:
                sosu = True
        if not sosu:
            sum+=1
    return sum 
