from itertools import permutations

n = int(input())

arr =[list(input().split()) for _ in range(n)]

count = 0
for permutation in permutations(range(1,10),3):
    good = True
    for i in range(n): #세로돌기
        strike = 0
        ball = 0
        for j in range(3):
            if int(arr[i][0][j]) == permutation[j]: #스트라익 일 경우
                strike +=1
                continue #스트라익일 경우 ball 검사 할 필요 없음
            if int(arr[i][0][j]) in permutation : # 해당 숫자가 permu 에 있을 경우
                ball+=1

        if strike != int(arr[i][1]): #해당 열의 strike 랑 ball 숫자가 둘다 같은지 검사
            good = False
        if ball != int(arr[i][2]):
            good = False

    if good : #전체 질문이랑 puermu 의 strike , ball 개수가 같을때
        count+=1

print(count)
