import sys
import itertools
input = sys.stdin.readline

n,m =map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
chicken = []
room = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i,j))
        elif arr[i][j] == 1:
            room.append((i,j))
result_chicken = list(itertools.combinations(chicken,m))
result = 2e9
for i in result_chicken: #m개 조합
    min_dist = 0 #m 개 합
    for j in room: #하나집과 치킨집 m 개중 젤 작은 거리
        temp = 2e9
        for k in i:
            temp = min(temp,abs(j[0]-k[0])+abs(j[1]-k[1])) #해당 조합 내의 치킨집중 가장 거리 작은거
        min_dist+=temp
    result= min(result,min_dist)
print(result)
