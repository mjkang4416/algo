def solution(land):
    answer = 0
    for i in range(1,len(land)):
        for j in range(len(land[0])): #바로 윗열, 자기자신 뺸 배열 만듬
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:] ) 
            #해당 배열최댓값 + 자신
    return max(land[-1])