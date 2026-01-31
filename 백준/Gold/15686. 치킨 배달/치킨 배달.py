import sys
from collections import deque
input = sys.stdin.readline
#중복있게 n 중  m개를 고른 수열 -> 중복조합
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
#2를 m 개 고를때 1 과 2의 거리의 최솟값
chicken_arr = []
houses = []
answer = float('inf')
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken_arr.append((i,j))
        if arr[i][j] ==1:
            houses.append((i,j))


def combination(cnt,start,minus_arr):
    if cnt == m:
        sum_chicken_dist(list(minus_arr)) #치킨집 조합
        return

    for i in range(start,len(chicken_arr)):
        temp = chicken_arr[i]
        minus_arr.append((temp[0],temp[1]))
        combination(cnt+1,i+1,minus_arr)
        minus_arr.pop()

def sum_chicken_dist(minus_arr):
    result = 0
    global answer
    for house in houses:
        dist = float('inf')
        for chicken_house in minus_arr: #조합별 집들과의 거리
            house_x = house[0]
            house_y = house[1]
            chicken_house_x = chicken_house[0]
            chicken_house_y = chicken_house[1]
            dist = min(dist,abs(house_x-chicken_house_x)+abs(house_y-chicken_house_y))
        result+=dist

    answer = min(answer,result)

combination(0,0,[])

print(answer)