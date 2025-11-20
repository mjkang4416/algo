from itertools import combinations, permutations

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

narr = []
for i in range(n):
    narr.append(i)

perm = list(combinations(narr,n//2)) # 조합 list

minNum = 1000000

for numlist in perm : #조합 하나 뽑기
    anotherNumList =[]
    team1 = 0
    team2 = 0
    for i in narr :
        if i in numlist :
            continue
        anotherNumList.append(i)  #

    combi1 = list(permutations(numlist,2)) #순열
    combi2 = list(permutations(anotherNumList,2)) #순열
    for j in combi1 : #콤비 더하기
        team1 += arr[j[0]][j[1]]
    
    for j in combi2 : #콤비 더하기
        team2 += arr[j[0]][j[1]]

    minNum = min(minNum,abs(team1-team2))


print(minNum)